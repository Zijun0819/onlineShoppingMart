from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve  # 上传文件处理函数

from .settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('df_goods.urls', 'df_goods'), namespace='df_goods')),  # 使用 app_name 和 namespace
    path('user/', include(('df_user.urls', 'df_user'), namespace='df_user')),
    path('cart/', include(('df_cart.urls', 'df_cart'), namespace='df_cart')),
    path('order/', include(('df_order.urls', 'df_order'), namespace='df_order')),
    path('tinymce/', include('tinymce.urls')),  # 使用富文本编辑框配置
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 使用 re_path 替代 url
]
