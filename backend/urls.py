from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index),
    path('multifile/', views.multifile),
    path('sdsResolve/', views.sdsResolve),
    path('getOpenid/', views.getOpenid),
    path('login/', views.login),
    path('test/', views.test),  # 13题测试入口不用管
    path('multifile2/', views.multifile2),  # 基础版moca测试文件及结果上传接口
]
