
from django.contrib import admin
from django.urls import path, include   # ←, includeを追加

urlpatterns = [
    path('manager/', include('manager.url')),   # ←ここを追加
    path('admin/', admin.site.urls),
]