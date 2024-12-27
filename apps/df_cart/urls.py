#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from . import views

app_name = 'df_cart'

urlpatterns = [
    path('', views.user_cart, name="cart"),  # 首页路径
    re_path(r'^add(\d+)_(\d+)/$', views.add, name="add"),  # 使用正则匹配
    re_path(r'^edit(\d+)_(\d+)/$', views.edit, name="edit"),  # 使用正则匹配
    re_path(r'^delete(\d+)/$', views.delete, name="delete"),  # 使用正则匹配
]

