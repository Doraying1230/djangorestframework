from rest_framework import serializers
from .models import Goods, GoodsCategory, GoodsImage


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 使用rest_framework 序列化
class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    # 关联子表
    images = GoodsImageSerializer(many=True)


    class Meta:
        model = Goods

        fields = "__all__"

    name = serializers.CharField(max_length=100)
    # 点击数
    click_num = serializers.IntegerField(default=0)
    # 销售量
    sold_num = serializers.IntegerField(default=0)
    # 封面，自动帮我在图片的路径前面加上media
    goods_fron_image = serializers.ImageField(default="")


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        # Model
        model = GoodsCategory
        # 把所有的属性都用上的写法
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    # 子目录，在models中related_name="sub_cat"
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        # Model
        model = GoodsCategory
        # 把所有的属性都用上的写法
        fields = "__all__"


# 商品类别序列化期
class CategorySerializer(serializers.ModelSerializer):
    # 子目录，在models中related_name="sub_cat"
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        # Model
        model = GoodsCategory
        # 把所有的属性都用上的写法
        fields = "__all__"
