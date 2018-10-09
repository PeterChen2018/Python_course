# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect

from django.shortcuts import render, render_to_response
from .models import Goods, Shop, GoodsShop, GoodsRecord, Backup, GoodsAddRecord, GoodsSellRecord, InboundChannel, \
    Cart, Order, GoodsReturnRecord, OtherCost, TransferShop, TransferRecord, ChangeCountRecord, RefundRecord

import datetime


def mylogin(request):
    if request.method == 'GET':
        return render_to_response('login.html')
    elif request.method == 'POST':
        next = request.GET.get('next', '/kucun/all/goods/')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse('帳號被鎖定！')
        else:
            return HttpResponseRedirect(reverse('login_fail'))


def login_fail(request):
    return render_to_response('login_fail.html', {'request': request, 'title': '登錄失敗'})


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mylogin'))

def out_in(request):
    today = datetime.date.today()
    every_day_sell_records = []
    for i in range(0, 10):
        that_day = today - datetime.timedelta(days=i)
        goods_records = GoodsRecord.objects.filter(date__year=that_day.year, date__month=that_day.month,
                                                   date__day=that_day.day).order_by('-date')
        day_and_records_map = {'date': that_day, 'records': goods_records}
        every_day_sell_records.append(day_and_records_map)
    header = title = '進出庫記錄'
    return render_to_response('out_in.html',
                              {'request': request, 'every_day_sell_records': every_day_sell_records, 'header': header,
                               'title': title})

def all_goods(request):
    goods = Goods.objects.filter(is_delete=False).order_by('goods_name')
    datas = []
    amount = 0
    for good in goods:
        kadi = GoodsShop.objects.get(goods=good, shop__name='卡迪電子')
        m = {'goods': good, 'kadi': kadi}
        amount += kadi.remain
        datas.append(m)
    shang = len(goods) / 3
    yu = len(goods) % 3
    if yu != 0:
        shang += 1

    return render_to_response('all_goods.html',
                              {'request': request, 'data1': datas[:shang], 'data2': datas[shang:shang * 2],
                               'data3': datas[shang * 2:], 'title': '卡迪管理系统', 'header': '卡迪管理系统', 'amount': amount})


def out(request):
    today = datetime.date.today()
    every_day_sell_records = []
    for i in range(0, 10):
        that_day = today - datetime.timedelta(days=i)
        goods_records = GoodsRecord.objects.filter(date__year=that_day.year, date__month=that_day.month,
                                                   date__day=that_day.day, change_num__lte=0).order_by('-date')

        day_and_records_map = {'date': that_day, 'records': goods_records}
        every_day_sell_records.append(day_and_records_map)
    header = title = '進庫記錄'
    return render_to_response('out_in.html',
                              {'request': request, 'every_day_sell_records': every_day_sell_records, 'header': header,
                               'title': title})


def in_(request):
    today = datetime.date.today()
    every_day_sell_records = []
    for i in range(0, 10):
        that_day = today - datetime.timedelta(days=i)
        goods_records = GoodsRecord.objects.filter(date__year=that_day.year, date__month=that_day.month,
                                                   date__day=that_day.day, change_num__gte=0).order_by('-date')

        day_and_records_map = {'date': that_day, 'records': goods_records}
        every_day_sell_records.append(day_and_records_map)
    header = title = '出庫記錄'
    return render_to_response('out_in.html',
                              {'request': request, 'every_day_sell_records': every_day_sell_records, 'header': header,
                               'title': title})