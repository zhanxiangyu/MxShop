# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-1-28 下午6:55'

import os
import sys
import django

from db_tools.data.product_data import row_data

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd+'../')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

django.setup()

from goods.models import Goods, GoodsCategory, GoodsImage


for goods_detail in row_data:
    goods_install = Goods()
    goods_install.name = goods_detail['name']
    goods_install.market_price = float(int(goods_detail['market_price'].replace("￥", "").replace("元", "")))
    goods_install.shop_price = float(int(goods_detail['sale_price'].replace("￥", "").replace("元", "")))
    goods_install.goods_brief = goods_detail['desc'] and goods_detail['desc'] or ''
    goods_install.goods_desc = goods_detail['goods_desc'] and goods_detail['goods_desc'] or ''
    goods_install.goods_front_image = goods_detail['images'][0] if goods_detail['images'] else ""

    categorys_name = goods_detail['categorys'][-1]
    category = GoodsCategory.objects.filter(name=categorys_name)
    if category:
        goods_install.category = category[0]
    goods_install.save()

    for goods_image in goods_detail['images']:
        goods_image_instace = GoodsImage()
        goods_image_instace.image = goods_image
        goods_image_instace.goods = goods_install
        goods_image_instace.save()


