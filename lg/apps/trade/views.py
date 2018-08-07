from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from trade.models import ShopingCart
from utils.permissions import IsOwnerOrReadOnly
from .serializers import ShopingCartSerializer, ShopingCartDetailSerializer


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
