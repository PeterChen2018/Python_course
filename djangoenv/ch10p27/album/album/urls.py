# -*- coding: utf-8 -*-
"""album URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from albumapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^albumshow/(\d+)/$', views.albumshow),
    url(r'^albumphoto/(\d+)/(\d+)/$', views.albumphoto),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^adminmain/$', views.adminmain),
    url(r'^adminmain/(\d+)/$', views.adminmain),
    url(r'^adminadd/$', views.adminadd),
    url(r'^adminfix/(\d+)/$', views.adminfix),
    url(r'^adminfix/(\d+)/(\d+)/$', views.adminfix),
    url(r'^adminfix/(\d+)/(\d+)/(\w+)/$', views.adminfix),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)