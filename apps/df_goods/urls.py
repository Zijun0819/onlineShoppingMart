from django.urls import path, re_path
from . import views

app_name = 'df_goods'

urlpatterns = [
    path('', views.index, name="index"),  # 首页路径
    re_path(r'^list(\d+)_(\d+)/$', views.good_list, name="good_list"),  # 列表页路径
    re_path(r'^(\d+)/$', views.detail, name="detail"),  # 详情页路径
    re_path(r'^search/', views.ordinary_search, name="ordinary_search"),  # 全文检索
]
