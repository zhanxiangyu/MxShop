# -*- coding:utf-8 -*-
# __author__ = 'zhan'
# __date__ = '18-1-25 下午10:14'

import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["singer_name", "singer_mobile", "district", "address"]

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)