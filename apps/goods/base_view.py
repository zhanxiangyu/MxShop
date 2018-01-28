# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-1-28 下午9:47'

import json
from django.views.generic.base import View
from django.http import JsonResponse

from goods.models import Goods


class GoodsListView(View):
    """
    通过django的view实现商品列表页
    """
    def get(self, request):
        goods = Goods.objects.all()

        from django.core import serializers
        json_list = serializers.serialize('json', goods)
        json_list = json.loads(json_list)
        # 不加safe参数无法序列化非字典对象
        return JsonResponse(json_list, safe=False)