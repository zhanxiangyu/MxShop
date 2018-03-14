# -*- coding:utf-8 -*-
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from goods.serializers import Goodserializer
from .models import Goods


class GoodsListView(APIView):
    """
    编写基础的api view
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        serializer = Goodserializer(goods, many=True)
        return Response(serializer.data)