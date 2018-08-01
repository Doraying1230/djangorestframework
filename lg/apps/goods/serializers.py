from rest_framework import serializers


# 使用rest_framework 序列化
class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    # 点击数
    click_num = serializers.IntegerField(default=0)
    # 销售量
    sold_num = serializers.IntegerField(default=0)
    # 封面，自动帮我在图片的路径前面加上media
    goods_fron_image = serializers.ImageField(default="")
