# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from .models import Goods, Shop, GoodsShop, GoodsRecord, Backup, GoodsAddRecord, GoodsSellRecord, InboundChannel, \
    Cart, Order, GoodsReturnRecord, OtherCost, TransferShop, TransferRecord, ChangeCountRecord, RefundRecord


def all_goods(request):
    goods = Goods.objects.filter(is_delete=False).order_by('goods_name')
    datas = []
    amount = 0
    for good in goods:
        kadi = GoodsShop.objects.get(goods=good, shop__name='卡迪电子')
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

