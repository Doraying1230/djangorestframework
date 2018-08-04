from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from .models import Goods, GoodsCategory
from .serializers import GoodsSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GoodsFilter
from rest_framework import filters


class CategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class GoodsListPagination(PageNumberPagination):
    # 默认返回10条
    page_size = 12
    # 每页返回多少条的参数变量
    page_size_query_param = 'page_size'
    page_query_param = "page"  # 页的字段
    # 最大返回100条
    max_page_size = 100


# GenericViewSet
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    返回商品列表,自定义序列化器，分页,过滤,搜索，排序
    """
    # 得到所有的商品
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination
    filter_class = GoodsFilter

    # 支持搜索和过滤，写在一起
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
    # 搜索的关键字从这些字段取
    # ^name,例如搜索水果，那么name字段中必然是水果开头才会满足条件
    # =name,精确搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')
    # 搜索字段
    ordering_fields = ('shop_price', 'sold_num')

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     filter_class = GoodsFilter
#
#     filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
#
#     search_fields = ('name', 'goods_brief', 'good_desc')
#
#     ordering_fields = ('shop_price', 'sold_num')


# GenericViewSet

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     返回商品列表,自定义序列化器，分页,过滤,搜索，排序
#     """
#     # 支持搜索和过滤，写在一起
#     filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
#     ordering_fields = ('shop_price', 'add_time')

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     返回商品列表,自定义序列化器，分页,过滤,搜索，排序
#     """
#     # 支持搜索和过滤，写在一起
#     filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
#     ordering_fields = ('shop_price', 'add_time')

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     queryset = Goods.objects.all()
#
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsListPagination
#
#     filter_class = GoodsFilter
#
#     filter_backends = (filters.SearchFilter, DjangoFilterBackend)
#
#     search_fields = ('^name', 'goods_brief', 'goods_desc')

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     返回商品列表
#     """
#     # 得到所有的商品
#     queryset = Goods.objects.all()
#     # 序列化期
#     serializer_class = GoodsSerializer
#     # 添加分页配置,settings.py就可以省略了
#     pagination_class = GoodsListPagination
#     # filter_backends = (DjangoFilterBackend,)
#     # filter_fields = ('name', 'shop_price')
#
#     filter_class = GoodsFilter

# class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
#     """
#     返回商品列表,自定义序列化器，分页,过滤,搜索，排序
#     """
#     # 支持搜索和过滤，写在一起
#     queryset = Goods.objects.all()
#         # 序列化期
#     serializer_class = GoodsSerializer
#     # 添加分页配置,settings.py就可以省略了
#     pagination_class = GoodsListPagination
#     # filter_backends = (DjangoFilterBackend,)
#     # filter_fields = ('name', 'shop_price')
#     filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
#     ordering_fields = ('shop_price', 'add_time')
