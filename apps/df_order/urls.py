#!/user/bin/env python
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from . import views

app_name = 'df_order'

urlpatterns = [
    path('', views.order, name="order"),
    re_path(r'^push/$', views.order_handle, name="push"),
]