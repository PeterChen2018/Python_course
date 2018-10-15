# -*- coding: utf-8 -*-
from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

from .models import Category, Product


"""
def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	
"""

def get_allsessions(request,key=None):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	


def get_session(request,key=None):
	if key in request.session:
		return HttpResponse('%s : %s' %(key,request.session[key]))
	else:
		return HttpResponse('Session 不存在!')


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
	return render(request, 'shop/product/login.html', locals())


def mylogout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop:mylogin'))


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'shop/product/detail.html', context)


