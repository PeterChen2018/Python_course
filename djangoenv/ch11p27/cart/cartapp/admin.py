# -*- coding: utf-8 -*-
from django.contrib import admin
from cartapp import models

admin.site.register(models.ProductModel)
admin.site.register(models.OrdersModel)
admin.site.register(models.DetailModel)