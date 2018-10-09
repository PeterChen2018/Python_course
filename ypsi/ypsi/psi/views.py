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

from psi import yforms
from yforms import YLogin

def ypsi_depots_in(request):
    act = request.GET.get("act","list")
    iId = request.GET.get("id","")
    pname = ""
    # level = request.user.get_profile().level
    level = 1 # 董事
    page_title = "入库单列表"
    if act == "add":
        page_title = "新增入庫提要資料"
        if request.POST:
            form = yforms.InStream(request.POST)
            if form.is_valid():
                fc = form.cleaned_data
                InStream(code=fc["code"],supplier=fc["supplier"],date=fc["date"],keeper=fc["keeper"],staff1=fc["staff1"],note=fc["note"]).save()
                return HttpResponseRedirect("?act=added")

        else:
            form = yforms.InStream()
        return render_to_response('app/depots_instream.html',{"page_title":page_title,"form":form,"act":act})

    elif act == "edit":
        page_title = "修改入库提要信息"
        ins = get_object_or_404(InStream, id=iId)
        user = request.user.get_profile().id
        if request.POST:
            form = yforms.InStream(request.POST)
            if form.is_valid():
                fc = form.cleaned_data
                if (ins.code<>fc["code"]) or (ins.supplier<>fc["supplier"]) or (ins.date<>fc["date"]) or (ins.keeper<>fc["keeper"]) or (ins.staff1<>fc["staff1"]) or (ins.hidden<>fc["hidden"]) or (ins.note<>fc["note"]) :
                    ins.code=fc["code"]
                    ins.supplier=fc["supplier"]
                    ins.date=fc["date"]
                    ins.keeper=fc["keeper"]
                    ins.staff1=fc["staff1"]
                    ins.hidden=fc["hidden"]
                    ins.note=fc["note"]
                    ins.save()
                return HttpResponseRedirect("?act=edited")
            
        else:
            form = yforms.InStream({"code":ins.code,"supplier":ins.supplier,"date":ins.date,"keeper":user,"staff1":ins.staff1_id,"hidden":ins.hidden,"note":ins.note,"log":ins.log})
        return render_to_response('app/depots_instream.html',{"page_title":page_title,"form":form,"act":"edit","iId":iId})

    elif act == "del":
        msg = "fail"
        if request.method == "POST":
            instream = get_object_or_404(InStream, id=request.POST.get("id",""))
            instream.hidden = True
            instream.save()
            msg = "success"
        return HttpResponse(msg, mimetype="text/plain")


    elif act == "d_add":
        product = get_object_or_404(Products, id=request.POST.get("pid",""))
        depot = get_object_or_404(Depot, id=request.POST.get("depot",""))
        ins = get_object_or_404(InStream, id=request.POST.get("insid",""))
        note = request.POST.get("note","")
        value = request.POST.get("value","")
        quantity = request.POST.get("quantity","")
        
        msg = []
        flag = True
        idid = ""
        regV = re.match(ur"^\d+\.?\d{0,2}$",value)
        if regV is None:
            flag = False
            msg.append("产品价格错误")
        regQ = re.match(ur"^[1-9][0-9]*$",quantity)
        if regQ is None:
            flag = False
            msg.append("产品数量错误")
        if len(note)>100:
            flag = False
            msg.append("位置详细信息超过100字符")
        if flag:
            ind = InDetail(inid=ins,product=product,value=value,quantity=quantity,depot=depot,depotdetail=note)
            ind.save()
            idid = ind.id
        return HttpResponse(simplejson.dumps({"flag":flag,"id":idid,"msg":"</br>".join(msg)},ensure_ascii=False), mimetype="text/plain")
        
        
    elif act=="d_del":
        idId = request.POST.get("id","")
        ind = get_object_or_404(InDetail, id=idId)
        flag = True
        if ind.product.p_str[3] - ind.quantity >ind.product.p_str[4]:
            ins = ind.inid
            if ins.log is None:
        	    ins.log = ""
            ins.log = u"%s %s 删除 产品：%s\n原:%s套 单价%s 仓库%s\n%s\n"\
            %(datetime.date.today(),request.user.get_profile().name,ind.product.name,ind.quantity,ind.value,ind.depot.name,31*'-') + ins.log
            ins.save()
            ind.delete()
        else:
            flag = False
        return HttpResponse(flag, mimetype="text/plain")
    elif act =="d_edit":
        idId = request.POST.get("id","")
        ind = get_object_or_404(InDetail, id=idId)
        depot = get_object_or_404(Depot,id=request.POST.get("depot",""))
        msg = []
        flag = True
        value = request.POST.get("value","")
        quantity = request.POST.get("quantity","")
        depotdetail = request.POST.get("depotdetail","")
        regV = re.match(ur"^\d+\.?\d{0,2}$",value)
        if regV is None:
            flag = False
            msg.append("产品价格错误")
        regQ = re.match(ur"^[1-9][0-9]*$",quantity)
        if regQ is None:
            flag = False
            msg.append("产品数量错误")
        if flag:
            if ind.quantity-int(quantity) > ind.product.p_str[1]:
                flag=False
                msg.append("修改后入库总数不可小于出库总数")
            d_in = InDetail.objects.filter(product=ind.product,depot=depot,inid__in=InStream.objects.filter(hidden=0)).aggregate(Sum('quantity'))["quantity__sum"]
            d_out = OutDetail.objects.filter(product=ind.product,depot=depot,outid__in=OutStream.objects.filter(hidden=0)).aggregate(Sum('quantity'))['quantity__sum']
            if d_out is None:
                d_out = 0
            if d_in is None:
                d_in = 0
            if (ind.quantity-int(quantity)) > (d_in-d_out):
                flag=False
                msg.append("修改后当前仓库入库总数不可小于出库总数,最大可修改值为%s"%(ind.quantity-(d_in-d_out)))

        if flag:
            if (ind.quantity <> quantity) or (ind.value <> value) or (ind.depot <> depot) or (ind.depotdetail <> depotdetail):
                ins = ind.inid
                if ins.log is None:
                    ins.log = ""
                ins.log = u"%s %s 修改 产品：%s\n原:%s套 单价%s 仓库%s\n新:%s套 单价%s 仓库%s\n%s\n"\
                %(datetime.date.today(),request.user.get_profile().name,ind.product.name,ind.quantity,ind.value,ind.depot.name,quantity,value,depot.name,31*'-') + ins.log
                ind.quantity = quantity
                ind.value = value
                ind.depot = depot
                ind.depotdetail = depotdetail
                ind.save()
                ins.save()
        return HttpResponse(simplejson.dumps({"flag":flag,"msg":"</br>".join(msg)},ensure_ascii=False), mimetype="text/plain")

    else:
        url = ""
        instream = ""
        if act == "detail":
            page_title="入库详单"
            instream = get_object_or_404(InStream, id=iId)
            ins = InDetail.objects.filter(inid=instream,quantity__gt=0).order_by("-id")
            url = "act=%s&id=%s&"%(act,iId)
        
        else:
            if act == "search":
                pid = get_object_or_404(Products, id=iId)
                pname = pid.name
                did=request.GET.get("did","0")
                if did == "0":
                    inds = InDetail.objects.filter(product=pid,quantity__gt=0).values_list("inid")
                else:
                    inds = InDetail.objects.filter(product=pid,quantity__gt=0,depot=did).values_list("inid")
                ins = InStream.objects.filter(id__in=inds).order_by("-id")
                slist = InDetail.objects.filter(inid__in=ins,quantity__gt=0,product=pid).values("inid","product").annotate(tq=Sum("quantity")).order_by("-inid")
                for (i,q) in zip(ins,slist):
                    i.pq = q["tq"]
                url = "act=search&id=%s&did=%s&"%(iId,did)
            else:
                ins = InStream.objects.order_by("-id")
        paginator = Paginator(ins, 20)
        after_range_num = 5      #当前页前显示5页
        befor_range_num = 4      #当前页后显示4页
        try:#如果请求的页码少于1或者类型错误，则跳转到第1页
            page = int(request.GET.get("page",1))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        ins_list = paginator.page(page)
        #if page >= after_range_num:
        #    page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
        #else:
        #    page_range = paginator.page_range[0:int(page)+befor_range_num]

        return render_to_response('app/depots_instream.html',{"page_title":page_title,"ins_list":ins_list,"rows":len(ins),"instream":instream,"level":level,"url":url,"pname":pname})


def ypsi_category(request):
    act = request.GET.get("act","")
    if act == "list":
        jsonclist = []
        if 'id' in request.GET:
            pid = request.GET["id"]
            cjlist = Category.objects.filter(hidden=0,pid=pid)
        else :
            cjlist = Category.objects.filter(hidden=0)


        for cj in cjlist:
            #c = {}
            #c['id'] = cj.id
            if cj.pid_id:
                jsonclist.append({"id":cj.id,"pId":cj.pid_id,"name":cj.name})
                #c['pId'] = cj.pid_id
            else:
                jsonclist.append({"id":cj.id,"pId":0,"name":cj.name})
                #c['pId'] = 0
            #c['name'] = cj.name

            #jsonclist.append(c)
        return HttpResponse(simplejson.dumps(jsonclist), mimetype='application/json')

    elif act=="edit":
        if request.method == 'POST':
            #print request.raw_post_data
            clist = eval(request.raw_post_data)

            cid_list = []
            cid_old_list=[]
            for c in clist:
                 cid_list.append(c['id'])

            c_old = Category.objects.all()
            for cd in c_old:
                cid_old_list.append(cd.id)

            cid_old_list.sort()
            cid_list.sort()

            cid_old_list_set = set(cid_old_list)
            cid_list_set = set(cid_list)

            #更新分类数据
            cid_list_x = cid_old_list_set & cid_list_set #提取更新部分ID
            c1 = Category.objects.filter(id__in=cid_list_x)#初步筛选
            for c in clist:
                try:
                    c1c = c1.get(id=c['id'])
                    if not (c1c.name == unicode(c['name'],'UTF-8') and c1c.pid_id == c['pId']):#加入判断，减少数据库写操作
                        #print c['name']
                        c1c.name=unicode(c['name'],'UTF-8')
                        if c["pId"] == None:
                            c1c.pid = None
                        else:
                            c1c.pid=get_object_or_404(Category,id=c['pId'])
                        c1c.save()
                except Exception as error:#因新分类库可能大于原有分类库，故会出现"not exist"错误，在此抛出
                    #print error
                    continue

            #删除分类,未完全完成下属分类产品标记删除
            cid_list_x = cid_old_list_set - cid_list_set #提取被删除部分ID
            c_del = Category.objects.filter(id__in=cid_list_x)
            c_del.update(hidden=True)
            Products.objects.filter(category__in=c_del).update(hidden=True)


            #新增分类
            cid_list_x = cid_list_set - cid_old_list_set #提取新增部分ID
            for c in clist:
                try:
                    cid_list_x.remove(c['id'])#set无直接索引办法，故使用删除，然后异常抛出处理
                    c_add = Category(name=unicode(c['name'],'UTF-8'),pid=get_object_or_404(Category,id=c['pId']))
                    c_add.save()
                    for i in range(len(clist)):#更新原始数据中的pId值，避免数据库开销
                        if clist[i]['pId'] == c['id']:
                            clist[i]['pId'] = c_add.id
                except Exception as error:
                    continue
        return HttpResponse(simplejson.dumps({"flag":True}), mimetype='application/json')
    else:
        page_title = "类别管理"
        # level = request.user.get_profile().level
        level = 1 # 董事
        return render_to_response("app/category.html",{"page_title":page_title,"level":level})

def ypsi_depots(request): # 查询店铺库存时产品 当前店铺库存项目 循环不合理，待修正
    page_title = "库存状况概览"
    act = request.GET.get("act","")
    qid = request.GET.get("id","")
    # level = request.user.get_profile().level
    level = 1 # 董事
    p_list = ""
    pd_list = ""
    st_list = ""
    page_range = ""
    if act:
        sdp_list = []
        stq_list = []
        cursor = connection.cursor()
        if (act == "shop" or act == "explort") and qid:
            shop = get_object_or_404(Shop,id=qid)
            page_title = u"%s 当前库存产品一览"%shop.name
            cursor.execute("select psi_outdetail.product_id,(sum(quantity)-ifnull(sq,0)) as tq from psi_outdetail,psi_outstream left join "
                            "(select product_id as spid,shop_id as ssid, sum(quantity) as sq from psi_sellorder,psi_sellorderdetail where psi_sellorder.hidden=0 and oid_id = psi_sellorder.id and ssid=%s group by spid) "
                            "on psi_outdetail.product_id=spid where psi_outstream.hidden=0 and psi_outstream.shop_id=%s and psi_outstream.id = outid_id  group by psi_outdetail.product_id order by product_id desc",[qid,qid])

        elif act == "depot" and qid and level<5:
            depot = get_object_or_404(Depot,id=qid)
            page_title = u"%s 当前库存产品一览"%depot.name
            cursor.execute("select psi_indetail.product_id,(sum(quantity)-ifnull(sq,0)) as tq from psi_indetail,psi_instream left join "
                            "(select product_id as spid,depot_id as odid, sum(quantity) as sq from psi_outstream,psi_outdetail where psi_outstream.hidden=0 and outid_id = psi_outstream.id and odid=%s group by spid) "
                            "on psi_indetail.product_id=spid  where psi_instream.hidden=0 and psi_indetail.depot_id=%s and psi_instream.id = inid_id  group by psi_indetail.product_id order by product_id desc",[qid,qid])

        sdp = cursor.fetchall()
        cursor.close()
        for s in sdp:
            sdp_list.append(s[0])
            stq_list.append(s[1])
        p_list = Products.objects.filter(hidden=0,id__in=sdp_list).order_by("-id")

        if request.GET.get("explort","") == "true":
            response = HttpResponse(mimetype="text/csv")
            response.write("\xEF\xBB\xBF")
            response["Content-Disposition"] = "attachment; filename=库存统计表.csv"
            writer = csv.writer(response)
            writer.writerow(["编号","名称","条码","尺寸","当前库存","仓库总库存","状态"])
            i = 1
            for p,s in zip(p_list,stq_list):
                i += 1
                if p.hidden == 1:
                    pStatus = u"已删除"
                else:
                    pStatus = u"正常"
                writer.writerow([i,p.name.encode('utf8'),p.barcode,p.size,s,p.p_str[1],pStatus.encode('utf8')])
            return response

        paginator = Paginator(p_list, 20)
        after_range_num = 5
        befor_range_num = 4
        try:
            page = int(request.GET.get("page",1))
            if page < 1:
                page = 1
        except ValueError:
            page = 1
        st_list = stq_list[20*(page-1):(20*page)] # 当前容器库存数
        pd_list = paginator.page(page)
        if page >= after_range_num:
            page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
        else:
            page_range = paginator.page_range[0:int(page)+befor_range_num]

    s_list = Shop.objects.exclude(name="总部").only("id","name")
    d_list = Depot.objects.filter(hidden=0).only("id","name")

    return render_to_response('app/depots.html',{"page_title":page_title,"s_list":s_list,"d_list":d_list,"p_list":p_list,"level":level,"r_list":pd_list,"st_list":st_list,"url":"?act=%s&id=%s"%(act,qid),"qid":qid,"page_range":page_range,"rows":len(p_list)})

def user_login(request):
    request.session.set_expiry(0) #关闭浏览器session失效
    act = request.GET.get("act","")
    err_count = request.session.get("err_count",0)
    page_title = "YPSI 系统登录"
    if err_count>5 and act!="stop":
        return HttpResponseRedirect('?act=stop')
    if act == "check":
        if request.method == 'POST':
            form=YLogin(request.POST.copy())
            if form.is_valid():
                form = form.cleaned_data
                name = form['username']
                pwd = form['password']
                # user = authenticate(username=name, password=pwd)
                next_path = request.session.get("next_path","")
                HttpResponseRedirect('%s'%next_path)
            else:
                page_title="表單填寫錯誤"

    elif act == "logout":
        logout(request)
        request.session.flush()
        return HttpResponseRedirect('/accounts/login/?act=out')
    elif act == "stop":
        page_title = "错误次数过多"
        form = ""
    else:
        if act == "out":
            page_title = "原登录信息已注销，可重新登录"
        elif act == "err":
            page_title="用户名或密码错误"
        form = YLogin()
        request.session["next_path"] = request.GET.get("next","")
    return render_to_response('accounts/login.html',locals())


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


def ypsi_staff(request):
    sid = request.GET.get("id","")
    act = request.GET.get("act","")
    if act == "pwd":
        if request.method == "POST":
            errmsg =""
            form =yforms.PWd(request.POST)
            user = get_object_or_404(User,id=request.POST.get("sid"))
            page_title = "密码修改中"
            if form.is_valid():
                pwd = request.POST.get("pwd")
                cd = form.cleaned_data
                if pwd==cd["pwd2"]:
                    if user.check_password(cd["opwd"]):
                        user.set_password(pwd)
                        user.save()
                        return HttpResponseRedirect("?act=pwd_changed")
                    else:
                        errmsg = "id_opwd,原密码错误。"
                else:
                    errmsg = "id_pwd,两次密码输入不一致。"
            return render_to_response("app/staff.html",{"page_title":page_title,"form":form,"errmsg":errmsg,"sid":request.POST.get("sid")})
            


        else:
            page_title = u"%s密码修改"%request.user.get_profile().name
            form =yforms.PWd()
            return render_to_response("app/staff.html",{"page_title":page_title,"form":form,"sid":request.user.id})


    else:
        page_title = "個人資料"
        staff = "test"
        staff_list = Staff.objects.filter(level__lt=99).order_by("-shop","level")
        if sid:
           staff =  get_object_or_404(Staff,id=sid)
        # else:
        #    staff = request.user.get_profile
        return render_to_response("app/staff.html",{"page_title":page_title,"staff_list":staff_list,"staff":staff})