# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'kucun'
__author__ = 'Test'

urlpatterns = [
    url(r'^$', views.all_goods, name='all_goods'),
    url(r'^all/goods/$', views.all_goods, name='all_goods'),
    url(r'^out/$', views.out, name='out'),
    url(r'^out_in/$', views.out, name='out_in'),
    url(r'^in/$', views.in_, name='in'),
    url(r'^login', views.mylogin, name='mylogin'),
    url(r'^accounts/login', views.mylogin, name='mylogin'),
    url(r'^logout/$', views.mylogout, name='logout'),
    url(r'^login/fail$', views.login_fail, name='login_fail'),
    url(r'^get_allsessions/$', views.get_allsessions),
    url(r'^get_session/(\w+)/$', views.get_session),
    url(r'^add/$', views.add_goods, name="add_goods"),
    url(r'^add/success$', views.add_success, name="add_success"),
    url(r'^transfer_shop_manage/$', views.transfer_shop_manage, name="transfer_shop_manage"),
    url(r'^api/delete_transfer_shop', views.delete_transfer_shop, name="delete_transfer_shop"),
    url(r'^api/add', views.api_add , name="api_add"),
    url(r'^api/sell', views.api_sell, name="api_sell"),
    url(r'^api/transfer', views.api_transfer, name="api_transfer"),
    url(r'^api/update/', views.api_update , name="api_update"),
    url(r'^api/update_count/', views.api_update_count , name="api_update_count"),
    
    
    
    
    
]




"""


__author__ = 'Test'

urlpatterns = patterns('',
                       url(r'^$', 'kucun.views.all_goods'),
                       url(r'^all/goods/$', 'kucun.views.all_goods', name='all_goods'),
                       url(r'^add/$', 'kucun.views.add_goods', name="addgoods"),
                       url(r'^add/success/$', 'kucun.views.add_success', name="addsuccess"),
                       url(r'^make_order/$', 'kucun.views.make_order', name="make_order"),
                       url(r'^inbound_channel/$', 'kucun.views.inbound_channel', name="inbound_channel"),
                       url(r'^transfer_shop_manage/$', 'kucun.views.transfer_shop_manage', name="transfer_shop_manage"),
                       url(r'^login/$', 'kucun.views.mylogin', name='mylogin'),
                       url(r'^login/fail$', 'kucun.views.login_fail', name='login_fail'),
                       url(r'^logout/$', 'kucun.views.mylogout', name="logout"),
                       
                       url(r'^api/sell/$', 'kucun.views.api_sell', name="api_sell"),
                       url(r'^api/transfer/$', 'kucun.views.api_transfer', name="api_transfer"),
                       url(r'^api/delete_sell_record/$', 'kucun.views.delete_sell_record', name="delete_sell_record"),
                       url(r'^api/delete_order_record/$', 'kucun.views.delete_order_record',
                           name="delete_order_record"),
                       url(r'^api/add/$', 'kucun.views.api_add', name="api_add"),
                       url(r'^api/sell_info/$', 'kucun.views.api_sell_info', name="api_sell_info"),
                       url(r'^api/order_info/$', 'kucun.views.api_order_info', name="api_order_info"),
                       url(r'^api/order_list/$', 'kucun.views.api_order_list', name="api_order_list"),
                       url(r'^api/change_arrears/$', 'kucun.views.api_change_arrears', name="api_change_arrears"),
                       url(r'^api/change_order_arrears/$', 'kucun.views.api_change_order_arrears',
                           name="api_change_order_arrears"),
                       url(r'^api/update/$', 'kucun.views.api_update', name="api_update"),
                       url(r'^api/update_count/$', 'kucun.views.api_update_count', name="api_update_count"),
                       url(r'^api/add_cart/$', 'kucun.views.add_cart', name="add_cart"),
                       url(r'^api/clean_cart', 'kucun.views.clean_cart', name="clean_cart"),
                       url(r'^api/delete_cart', 'kucun.views.delete_cart', name="delete_cart"),
                       url(r'^api/submit_cart', 'kucun.views.submit_cart', name="submit_cart"),
                       url(r'^api/delete_inbound', 'kucun.views.delete_inbound', name="delete_inbound"),
                       url(r'^api/delete_goods', 'kucun.views.delete_goods', name="delete_goods"),
                       url(r'^api/delete_transfer_shop', 'kucun.views.delete_transfer_shop', name="delete_transfer_shop"),
                       #
                       url(r'^outin/$', 'kucun.views.out_in', name="out_in"),
                       url(r'^out/$', 'kucun.views.out', name="out"),
                       url(r'^in/$', 'kucun.views.in_', name="in"),
                       url(r'^sell_record/$', 'kucun.views.sell_record', name="sell_record"),
                       url(r'^add_record/$', 'kucun.views.add_record', name="add_record"),
                       url(r'^today_profit/$', 'kucun.views.today_profit', name="today_profit"),
                       url(r'^yesterday_profit/$', 'kucun.views.yesterday_profit', name="yesterday_profit"),
                       url(r'^this_month_profit/$', 'kucun.views.this_month_profit', name="this_month_profit"),
                       url(r'^last_month_profit/$', 'kucun.views.last_month_profit', name="last_month_profit"),
                       url(r'^other_month_profit/$', 'kucun.views.other_month_profit', name="other_month_profit"),
                       url(r'^all_arrears/$', 'kucun.views.all_arrears', name="all_arrears"),
                       url(r'^order_arrears/$', 'kucun.views.order_arrears', name="order_arrears"),
                       url(r'^order_manage/$', 'kucun.views.order_manage', name="order_manage"),
                       url(r'^goods_return_record/$', 'kucun.views.goods_return_record', name="goods_return_record"),
                       url(r'^goods_transfer_record/$', 'kucun.views.transfer_record', name="transfer_record"),
                       url(r'^other_cost/$', 'kucun.views.other_cost', name="other_cost"),
                       url(r'^delete_goods/$', 'kucun.views.delete_goods', name="delete_goods"),

                       url(r'arrears/(\d+)/(\d+)/$', 'kucun.views.check_month_arrears', name='check_month_arrears'),

                       url(r'^cart_show', 'kucun.views.cart_show', name="cart_show"),

                       url(r'^chart/profit/$', 'kucun.views.profit_chart', name="profit_chart"),
                       url(r'^chart/sell_ranking/$', 'kucun.views.sell_ranking_chart', name="sell_ranking_chart"),
)
"""