# -*- coding: utf-8 -*-

import codecs
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

# from django.utils import simplejson
import json
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models.signals import post_save


from django.db import models
from .models import SellOrder,Shop,Depot,Products,Customer, Staff, SellOrderDetail,Remit,InStream,InDetail,OutStream,OutDetail, Category,Posts


def ypsi_index(request):
    request.session.set_expiry(0) #关闭浏览器session失效
    page_errs = ""
    # user = request.user.get_profile()
    # last_login = request.user.last_login
    # act = request.GET.get("act","")
    # wmode = request.GET.get("w","")
    # days = request.GET.get('days',7)
    # act = "getData"
    act = ""
    if page_errs == "":
        # dlist = ypsi_sell_list(days)[0]
        # s_str = ypsi_sell_list(days)[1]
        dlist = []
        s_str = []
        page_title = u"首页"
        plist = Posts.objects.filter(hidden=0).order_by("-id")
        slist = SellOrder.objects.filter(hidden=0).order_by("-id")[:10]
        if act == "getData":
            jStr = {"plist":[],"slist":[],"err":page_errs}
            for p in plist:
                jStr["plist"].append({"title":p.title,"note":p.note,"date":datetime.datetime.strftime(p.date,'%Y-%m-%d')})
            for s in slist:
                jStr["slist"].append({"sid":s.id,"shop":s.shop.name,"staff":s.staff.name,"amount":s.total,"date":datetime.datetime.strftime(s.date,'%Y-%m-%d %H:%M:%S')})
            # return HttpResponse(simplejson.dumps({"page_title":page_title,"plist":jStr["plist"],"slist":jStr["slist"],"dlist":dlist,"s_str":s_str},ensure_ascii=False), mimetype="text/plain")
            return HttpResponse(json.dumps({"page_title":page_title,"plist":jStr["plist"],"slist":jStr["slist"],"dlist":dlist,"s_str":s_str},ensure_ascii=False))
        else:
            # return render_to_response("app/index.html",{"page_title":page_title,"err":page_errs,"user":user,"last_login":last_login,"plist":plist,"slist":slist,"dlist":dlist,"s_str":s_str,"wmode":wmode})
            return render_to_response("app/index.html",{"page_title":page_title,"err":page_errs})
    else:
        return HttpResponse("<html><center>%s</center></html>"%page_errs)
