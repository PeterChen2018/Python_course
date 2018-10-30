# -*- coding: utf-8 -*-

"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.user_detail, name='user_detail'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^accounts/login', views.login, name='login'),
    url(r'^get_allsessions/$', views.get_allsessions),
]

#　
# @login_required(login_url='/kucun/login')
# def delete_goods(request):
# 
# def mylogin(request):
# 
# url(r'^api/delete_goods', 'kucun.views.delete_goods', name="delete_goods"),
# url(r'^login/$', 'kucun.views.mylogin', name='mylogin'),
# app_name = 'testap'
"""