from django.urls import path
from . import views

urlpatterns = [
    # path('index/', views.index),
    path('multifile/', views.multifile),
    path('sdsResolve/', views.sdsResolve),
    path('getOpenid/', views.getOpenid),
    path('login/', views.login),
     path('test/', views.test) # 13题测试入口不用管
]