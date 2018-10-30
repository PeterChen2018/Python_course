# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import UserProfile

def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	

"""
@login_required(login_url='/kucun/login')
def mylogin(request):
    if request.method == 'GET':
        # logout(request)
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
                return HttpResponse('账号被锁定！')
        else:
            return HttpResponseRedirect(reverse('login_fail'))

def login_fail(request):
    return render_to_response('login_fail.html', {'request': request, 'title': '登录失败'})

def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mylogin'))
"""
# @login_required(login_url='/loginapp/login')
# @login_required(login_url='/kucun/login')
# @login_required(login_url='/login/login')

@login_required
def user_detail(request):
	if request.user.is_authenticated:
	   name=request.user.username
	   first_name=request.user.first_name
	   last_name=request.user.last_name
	   email=request.user.email
	   is_active=request.user.is_active
	   is_staff=request.user.is_staff
	   last_login=request.user.last_login
	return render(request, "detail2.html", locals())

def index(request):
	if request.user.is_authenticated:
	   name=request.user.username
	   #first_name=request.user.first_name
	   #last_name=request.user.last_name
	   #email=request.user.email
	   #is_active=request.user.is_active
	   #is_staff=request.user.is_staff
	   #last_login=request.user.last_login
	   print name
	   print User.objects.get(username=name)
	   try:
	       user = User.objects.get(username=name)
	       print user
	       print 'userinfo'
	       print UserProfile.objects.get(user=user)
	       userinfo = UserProfile.objects.get(user=user)
	       print userinfo.user.username
	       print userinfo.accepted_eula
	       print userinfo.favorite_animal
	   except:
	       print 'pass'
	       pass
	return render(request, "index.html", locals())


def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())


def logout(request):
	auth.logout(request)
	return redirect('/index/')	

def adduser(request):
	try:
		user=User.objects.get(username="test")
	except:
		user=None
	if user!=None:
		# message = user.username + " 帳號已建立!"
		message = "User name: " + user.username + " is exist !"
		return HttpResponse(message)
	else:	# 建立 test 帳號
		user=User.objects.create_user("test","test@test.com.tw","aa123456")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')