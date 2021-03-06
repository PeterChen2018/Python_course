# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adate', models.DateTimeField(auto_now=True)),
                ('alocation', models.CharField(blank=True, default=b'', max_length=200)),
                ('atitle', models.CharField(max_length=100)),
                ('adesc', models.TextField(blank=True, default=b'')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psubject', models.CharField(max_length=100)),
                ('pdate', models.DateTimeField(auto_now=True)),
                ('purl', models.CharField(max_length=100)),
                ('phit', models.IntegerField(default=0)),
                ('palbum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albumapp.AlbumModel')),
            ],
        ),
    ]
