from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import UserFav
from .serializers import UserFavViewSerializer


class UserFavViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, GenericViewSet):
    """用户收藏"""
    # 用户列表
    queryset = UserFav.objects.all()
    # 指定序列化器
    serializer_class = UserFavViewSerializer
