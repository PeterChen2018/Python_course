# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^index/$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^login', views.login, name='login'),
    url(r'^accounts/login', views.login, name='login'),
    url(r'^logout/$', views.mylogout, name='logout'),
    # url(r'^get_allsessions/$', views.get_allsessions),
    url(r'^get_allsessions/(\w+)/$', views.get_allsessions),
    url(r'^get_session/(\w+)/$', views.get_session),
]
