# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User

import django.utils.timezone as timezone


class Shop(models.Model):
    name = models.CharField(max_length=20,help_text="店鋪名稱")
    telephone = models.CharField(max_length=11,help_text="電話")
    address = models.CharField(max_length=100,help_text="地址")
    opendate = models.DateTimeField('開業日期',default=timezone.now )
    note = models.CharField(max_length=100,blank=True,null=True,help_text="備註")
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = ('店舖管理')



class UserProfile(models.Model):
    user = models.OneToOneField(User) # 一對一的欄位,對應到User (必要)
    # 要加的欄位
    accepted_eula = models.BooleanField()
    favorite_animal = models.CharField(max_length=20, default='Dragon')
    def __unicode__(self):
        return self.favorite_animal
    class Meta:
        verbose_name_plural = ('人員管理')