# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psi', '0002_auto_20181004_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joindate',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe5\x8a\xa0\xe5\x85\xa5\xe6\x97\xa5\xe6\x9c\x9f', null=True),
        ),
        migrations.AlterField(
            model_name='instream',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='outstream',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe5\x8f\x91\xe8\x96\xaa\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='remit',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe6\xb1\x87\xe6\xac\xbe\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='opendate',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe5\xbc\x80\xe4\xb8\x9a\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='joindate',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 20, 20, 8, 60000), help_text=b'\xe5\x85\xa5\xe8\x81\x8c\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
    ]
