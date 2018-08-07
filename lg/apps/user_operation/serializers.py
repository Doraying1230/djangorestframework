from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import UserFav


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
