from rest_framework import serializers
from .models import Goods, ShopingCart


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
