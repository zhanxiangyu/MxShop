# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-3-18 下午7:12'

import django_filters

from .models import Goods

class GoodsFilter(django_filters.rest_framework.FilterSet):

    price_min = django_filters.NumberFilter(name='shop_price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(name='shop_price', lookup_expr='lte')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']