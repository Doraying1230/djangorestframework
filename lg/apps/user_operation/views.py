from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import UserFav
from .serializers import UserFavViewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import SessionAuthentication


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    """用户收藏"""
    # 用户列表
    queryset = UserFav.objects.all()
    # 指定序列化器
    serializer_class = UserFavViewSerializer
    # 配置权限校验，检验是否登录
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    # JWT
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)
    lookup_field = "goods_id"

    # 得到收藏的时候，只能让其得到当前用户的所有收藏，而不能得到其他用户的收藏
    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

