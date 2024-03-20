from django.contrib import admin
from django.urls import path, include
from tokyo03.views import Listtokyo03View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Listtokyo03View.as_view(), name='list_tokyo03'),  # 追加する行
    path('tokyo03/', include('tokyo03.urls')),
]
