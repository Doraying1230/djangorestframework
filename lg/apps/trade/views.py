from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import mixins
from trade.models import ShopingCart, OrderInfo, OrderGoods
from utils.alipay import AliPay
from utils.permissions import IsOwnerOrReadOnly
from .serializers import ShopingCartSerializer, ShopingCartDetailSerializer, OrderSerializer, OrderDetailSerializer
from rest_framework import views
from lg.settings import private_key_path, ali_public_path
from datetime import datetime
from rest_framework.response import Response
from django.shortcuts import redirect


class AlipayView(views.APIView):
    def get(self, request):
        """
          处理支付宝返回的return_url
          :param request:
          :return:
          """
        processed_dict = {}
        for key, value in request.GET.items():
            processed_dict[key] = value
        # 得到签名
        sign = processed_dict.pop("sign", None)

        alipay = AliPay(
            appid="2016091800542258",
            app_notify_url="http://127.0.0.1:8000/alipay/ruturn/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_public_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/alipay/ruturn/"
        )
        verify_result = alipay.verify(processed_dict, sign)
        if verify_result:
            # 该交易在支付宝系统中的交易流水号
            trade_no = processed_dict.get("trade_no")
            # 商户网站唯一订单号
            order_sn = processed_dict.get("out_trade_no")

            pay_status = processed_dict.get("pay_status", "TRADE_SUCCESS")

            orders = OrderInfo.objects.filter(order_sn=order_sn)

            for order in orders:
                order.trade_sn = trade_no
                # 修改状态
                order.pay_status = pay_status
                order.pay_time = datetime.now()

                order.save()
            # return Response("success")
            response = redirect("index")
            # 设置cookie
            response.set_cookie("nextPath", "pay", max_age=2)
            return response
        else:
            # 跳转到首页
            response = redirect("index")
            return response

    def post(self, request):
        """
        处理支付宝的notify_url
        :param request:
        :return:
        """
        pass


class OrderViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """订单管理
    list: 获取个人订单
    create:添加订单
    delete:删除订单
    retrieve:订单详情信息
    """
    # 这个时候删除某个地址的时候就会验证是否是对应用户的地址--IsOwnerOrReadOnly
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    # JWT认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 序列化器
    # serializer_class = OrderSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        else:
            return OrderSerializer

    def get_queryset(self):
        # 过滤得到当前用户的订单列表
        return OrderInfo.objects.filter(user=self.request.user)

    # 重新改方法用户提交订单
    def perform_create(self, serializer):
        order = serializer.save()
        # 得到当前用户购物车所有信息
        shop_carts = ShopingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            # 把数据和OrderGoods对应起来
            order_goods = OrderGoods()
            # 订单
            order_goods.order = order
            # 商品
            order_goods.goods = shop_cart.goods
            # 商品数量
            order_goods.goods_num = shop_cart.nums
            # 订单金额
            # 保存订单和商品关联的Model
            order_goods.save()

            # 把该条信息在购车中删除--订单提交后，清空购物车
            shop_cart.delete()


class ShopingCartViewSet(viewsets.ModelViewSet):
    # serializer_class = ShopingCartSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    # JWT认证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 设置支持外键字段http://127.0.0.1:8000/shopcarts/1/那么1就是商品id
    lookup_field = "goods_id"

    def get_queryset(self):
        return ShopingCart.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ShopingCartDetailSerializer
        else:
            return ShopingCartSerializer
