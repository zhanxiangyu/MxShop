# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-3-14 下午11:25'

from rest_framework import serializers


class Goodserializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=200)
    click_num = serializers.IntegerField(default=0)
    pass