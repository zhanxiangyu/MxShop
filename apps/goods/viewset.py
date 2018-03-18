# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-3-18 下午5:29'
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import mixins, filters
from rest_framework.pagination import PageNumberPagination

from .models import Goods, GoodsCategory
from .serializers import Goodserializer, CategorySerializer
from .filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'  # 页码查询参数
    page_size_query_param = 'page_size'  # 每页显示大小
    max_page_size = 20
    pass


class GoodsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = Goodserializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)  # 后面的字段不配置，怎起不到效果，就像DjangoFilterBackend没有配置字段，就没有效果
    filter_class = GoodsFilter  # 自定义过滤
    search_fields = ('name', 'goods_desc')  # 搜索字段
    ordering_fields = ('shop_price',)  # 排序字段
    ordering = ('-add_time')  # 默认排序
    pass


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    pass