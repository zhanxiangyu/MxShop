# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-3-14 下午11:25'

from rest_framework import serializers
from .models import GoodsCategory


class Goodserializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=200)
    click_num = serializers.IntegerField(default=0)
    pass


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'
