from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserFav
from goods.serializers import GoodsSerializer


class UserFavViewSerializer(serializers.ModelSerializer):
    """用户收藏"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # validators=[
        #     UniqueTogetherValidator(
        #         queryset=UserFav.objects.all(),
        #         fields=('user','goods')
        #     )
        # ]
        model = UserFav
        fields = ("user", "goods", "id")


class UserFavDetailSerializer(serializers.ModelSerializer):
    """用户收藏商品详细信息"""
    goods = GoodsSerializer()

    class Meta:
        # 使用代码验证提交的时候，有没有重复
        model = UserFav
        fields = ("goods", "id")
