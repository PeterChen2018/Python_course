# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

from accounts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.user_detail, name='user_detail'),
    url(r'^adduser/$', views.adduser, name='adduser'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login', views.login, name='login'),
    url(r'^accounts/login', views.login, name='login'),
    url(r'^get_allsessions/$', views.get_allsessions),
]

"""
登入登出由django內建auth.views.login/logout來處理, 註冊由自行建立的app 'accounts'處理
url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
url(r'^accounts/register/$', 'accounts.views.register', name='register'),
url(r'^accounts/profile/$', 'django.views.generic.simple.direct_to_template', {'template':'registration/profile.html'}, name='user_profile'),
"""