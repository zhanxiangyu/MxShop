# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-1-28 下午6:13'

import sys
import os
import django

from db_tools.data.category_data import row_data

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')

# 和manage.py文件的使用一样
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

# 启动django
django.setup()

from goods.models import GoodsCategory


for lev1_cat in row_data:
    lev1_install = GoodsCategory()
    lev1_install.code = lev1_cat['code']
    lev1_install.name = lev1_cat['name']
    lev1_install.category_type = 1
    lev1_install.save()

    for lev2_cat in lev1_cat['sub_categorys']:
        lev2_intance = GoodsCategory()
        lev2_intance.name = lev2_cat['name']
        lev2_intance.code = lev2_cat['code']
        lev2_intance.category_type = 2
        lev2_intance.parent_category = lev1_install
        lev2_intance.save()

        for lev3_cat in lev2_cat['sub_categorys']:
            lev3_install = GoodsCategory()
            lev3_install.name = lev3_cat['name']
            lev3_install.code = lev3_cat['code']
            lev3_install.category_type = 3
            lev3_install.parent_category = lev2_intance
            lev3_install.save()

print('insert data over!!!')

