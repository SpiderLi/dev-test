# _*_coding:utf-8_*_
"""
# @Author  : Guangqiang Li
# @Time    : 2021/7/7 16:53
# @Description:
"""
from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('captcha/', include('captcha.urls'))
]