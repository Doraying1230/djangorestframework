from rest_framework import serializers
from goods.serializers import GoodsSerializer
from .models import Goods, ShopingCart, OrderInfo, OrderGoods


# 一个订单对应多个商品，商品再把商品的详细信息列出
class OrderGoodsSerialzier(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


# 用的时候使用OrderSerializer和OrderDetailSerializer，
class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerialzier(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    """订单序列化器"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    # 订单号不让前端编写
    order_sn = serializers.CharField(read_only=True)
    # 交易号不让前端编写
    trade_sn = serializers.CharField(read_only=True)
    # 支付状态
    pay_status = serializers.CharField(read_only=True)
    # 支付时间
    pay_time = serializers.DateTimeField(read_only=True)
    # 添加时间
    add_time = serializers.DateTimeField(read_only=True)

    # 自定义生成订单号信息
    def generate_order_sn(self):
        import time
        from random import randint
        # "当前时间+userid+随机数"
        order_sn = "{time_str}{userid}{randstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                        userid=self.context["request"].user, randstr=randint(10, 99))
        return order_sn

    def validate(self, attrs):
        """取消订单"""
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = OrderInfo
        fields = "__all__"


class ShopingCartDetailSerializer(serializers.ModelSerializer):
    # 外键
    goods = GoodsSerializer(many=False)

    class Meta:
        model = ShopingCart
        fields = "__all__"


class ShopingCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # 商品数量
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={
        "required": "请选择购买的数量",
        "min_value": "购买数量最少为1"
    })
    # 商品
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())

    # 重写更新的方法
    def update(self, instance, validated_data):
        instance.nums = validated_data["nums"]
        instance.save()
        return instance

    # 自定义怎么保存购物车商品--重点
    def create(self, validated_data):
        # 要考虑：有记录和没有记录两种情况
        user = self.context["request"].user
        # 商品数量
        nums = validated_data["nums"]
        # 商品
        goods = validated_data["goods"]
        # 查询是否存在
        exised = ShopingCart.objects.filter(user=user, goods=goods)
        if exised:
            exised = exised[0]
            # 添加刚才的数量
            exised.nums += nums
            exised.save()  # 保存
        else:
            # 创建
            exised = ShopingCart.objects.create(**validated_data)
        return exised
