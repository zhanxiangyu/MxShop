# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-3-18 下午5:36'

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .viewset import GoodsViewSet

router = DefaultRouter()

router.register('goods', GoodsViewSet, base_name='goods')

urlpatterns = [
    url('^api/', include(router.urls), name='api')
]