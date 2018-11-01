# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 02:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe5\x88\x86\xe9\xa1\x9e\xe5\x90\x8d\xe7\xa8\xb1', max_length=10)),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x9a\xb1\xe8\x97\x8f')),
                ('pid', models.ForeignKey(blank=True, help_text=b'\xe7\x88\xb6\xe7\xb4\x9a\xe5\x88\x86\xe9\xa1\x9e', null=True, on_delete=django.db.models.deletion.CASCADE, to='psi.Category')),
            ],
            options={
                'verbose_name_plural': '\u5206\u985e\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe9\xa1\xbe\xe5\xae\xa2\xe5\xa7\x93\xe5\x90\x8d', max_length=10)),
                ('code', models.CharField(blank=True, help_text=b'\xe7\xbc\x96\xe5\x8f\xb7', max_length=20, null=True)),
                ('telephone', models.CharField(blank=True, help_text=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d', max_length=11, null=True)),
                ('address', models.CharField(blank=True, help_text=b'\xe5\x9c\xb0\xe5\x9d\x80', max_length=100, null=True)),
                ('joindate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8a\xa0\xe5\x85\xa5\xe6\x97\xa5\xe6\x9c\x9f')),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '\u987e\u5ba2\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe4\xbb\x93\xe5\xba\x93\xe5\x90\x8d', max_length=10)),
                ('address', models.CharField(help_text=b'\xe4\xbb\x93\xe5\xba\x93\xe5\x9c\xb0\xe5\x9d\x80', max_length=100)),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x9a\x90\xe8\x97\x8f')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '\u4ed3\u5e93\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='InDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, help_text=b'\xe5\xbb\xa0\xe6\x96\xb9\xe9\x80\xb2\xe5\x83\xb9', max_digits=8)),
                ('quantity', models.IntegerField(help_text=b'\xe6\x95\xb8\xe9\x87\x8f')),
                ('depotdetail', models.CharField(blank=True, help_text=b'\xe5\x87\xba\xe5\x85\xa5\xe5\xba\xab\xe8\xa9\xb3\xe7\xb4\xb0\xe4\xbd\x8d\xe7\xbd\xae', max_length=100, null=True)),
                ('depot', models.ForeignKey(help_text=b'\xe5\x87\xba\xe5\x85\xa5\xe5\xba\xab\xe5\xba\xab\xe6\x88\xbf', on_delete=django.db.models.deletion.CASCADE, to='psi.Depot')),
            ],
            options={
                'verbose_name_plural': '\u5165\u5eab\u8a73\u55ae',
            },
        ),
        migrations.CreateModel(
            name='InStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text=b'\xe5\x85\xa5\xe5\xba\xab\xe5\x96\xae\xe8\x99\x9f', max_length=30, unique=True)),
                ('supplier', models.SmallIntegerField(choices=[(1, b'\xe7\xbe\x85\xe8\x90\x8a'), (2, b'\xe5\x84\xaa\xe5\xae\xb6'), (3, b'\xe5\xaf\xb6\xe7\xb8\xb5'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')], help_text=b'\xe4\xbe\x9b\xe6\x87\x89\xe5\x95\x86')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100, null=True)),
                ('log', models.TextField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=1500, null=True)),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xaa\xe9\x99\xa4\xe6\xa8\x99\xe8\xa8\x98')),
            ],
            options={
                'verbose_name_plural': '\u5165\u5eab\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='OutDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('depot', models.ForeignKey(help_text=b'\xe5\x87\xba\xe5\x85\xa5\xe5\xba\x93\xe5\xba\x93\xe6\x88\xbf', on_delete=django.db.models.deletion.CASCADE, to='psi.Depot')),
            ],
            options={
                'verbose_name_plural': '\u51fa\u5e93\u8be6\u5355',
            },
        ),
        migrations.CreateModel(
            name='OutStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text=b'\xe5\x87\xba\xe5\xba\x93\xe5\x8d\x95\xe6\x8d\xae\xe5\x8f\xb7', max_length=30, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, help_text=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('returned', models.BooleanField(default=False, help_text=b'\xe9\x80\x80\xe5\xba\x93\xe6\xa0\x87\xe8\xae\xb0')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=100, null=True)),
                ('log', models.TextField(blank=True, help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=1500, null=True)),
            ],
            options={
                'verbose_name_plural': '\u51fa\u5e93\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='PaySlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay', models.DecimalField(decimal_places=2, help_text=b'\xe5\xb7\xa5\xe8\xb3\x87', max_digits=7)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe7\x99\xbc\xe8\x96\xaa\xe6\x97\xa5\xe6\x9c\x9f')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100)),
            ],
            options={
                'verbose_name_plural': '\u85aa\u8cc7\u767c\u653e\u8a18\u9304',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=20)),
                ('note', models.CharField(help_text=b'\xe5\x85\xac\xe5\x91\x8a\xe5\x86\x85\xe5\xae\xb9', max_length=100)),
                ('date', models.DateField(auto_now_add=True, help_text=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
            ],
            options={
                'verbose_name_plural': '\u516c\u544a\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa8\xb1', max_length=30)),
                ('barcode', models.CharField(blank=True, help_text=b'\xe6\xa2\x9d\xe5\xbd\xa2\xe7\xa2\xbc', max_length=20, null=True)),
                ('image', models.ImageField(blank=True, help_text=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9c\x96\xe7\x89\x87', null=True, upload_to=b'products')),
                ('size', models.CharField(blank=True, help_text=b"\xe5\xb0\xba\xe5\xaf\xb8,\xe8\xab\x8b\xe4\xbd\xbf\xe7\x94\xa8','\xe8\x99\x9f\xe5\x88\x86\xe5\x89\xb2,\xe5\xa6\x82230,180", max_length=20, null=True)),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xaa\xe9\x99\xa4\xe6\xa8\x99\xe8\xa8\x98')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100, null=True)),
                ('category', models.ForeignKey(help_text=b'\xe9\xa1\x9e\xe5\x88\xa5', on_delete=django.db.models.deletion.CASCADE, to='psi.Category')),
            ],
            options={
                'verbose_name_plural': '\u5546\u54c1\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Remit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.SmallIntegerField(choices=[(1, b'\xe7\xbe\x85\xe8\x90\x8a'), (2, b'\xe5\x84\xaa\xe5\xae\xb6'), (3, b'\xe5\xaf\xb6\xe7\xb8\xb5'), (4, b'\xe5\x85\xb6\xe4\xbb\x96')], help_text=b'\xe4\xbe\x9b\xe6\x87\x89\xe5\x95\x86')),
                ('amount', models.DecimalField(decimal_places=2, help_text=b'\xe9\x87\x91\xe9\xa2\x9d', max_digits=8)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8c\xaf\xe6\xac\xbe\xe6\x97\xa5\xe6\x9c\x9f')),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xaa\xe9\x99\xa4\xe6\xa8\x99\xe8\xa8\x98')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '\u532f\u6b3e\u8a18\u9304',
            },
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, help_text=b'\xe9\x94\x80\xe5\x94\xae\xe5\x8d\x95\xe6\x8d\xae\xe5\x8f\xb7', max_length=20, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, help_text=b'\xe6\x8a\x98\xe6\x89\xa3\xe9\x87\x91\xe9\xa2\x9d', max_digits=8, null=True)),
                ('date', models.DateTimeField(help_text=b'\xe6\x97\xa5\xe6\x9c\x9f')),
                ('hidden', models.BooleanField(default=False, help_text=b'\xe5\x88\xa0\xe9\x99\xa4\xe6\xa0\x87\xe8\xae\xb0')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\xa4\x87\xe6\xb3\xa8', max_length=100, null=True)),
                ('customer', models.ForeignKey(blank=True, help_text=b'\xe9\xa1\xbe\xe5\xae\xa2', null=True, on_delete=django.db.models.deletion.CASCADE, to='psi.Customer')),
            ],
            options={
                'verbose_name_plural': '\u9500\u552e\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='SellOrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(help_text=b'\xe6\x95\xb8\xe9\x87\x8f')),
                ('price', models.DecimalField(decimal_places=2, help_text=b'\xe5\x83\xb9\xe6\xa0\xbc', max_digits=8)),
                ('oid', models.ForeignKey(help_text=b'\xe9\x8a\xb7\xe5\x94\xae\xe5\x96\xae\xe6\x93\x9a\xe8\x99\x9f', on_delete=django.db.models.deletion.CASCADE, to='psi.SellOrder')),
                ('product', models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', on_delete=django.db.models.deletion.CASCADE, to='psi.Products')),
            ],
            options={
                'verbose_name_plural': '\u92b7\u552e\u8a73\u55ae',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe5\xba\x97\xe9\x8b\xaa\xe5\x90\x8d\xe7\xa8\xb1', max_length=20)),
                ('telephone', models.CharField(help_text=b'\xe9\x9b\xbb\xe8\xa9\xb1', max_length=11)),
                ('address', models.CharField(help_text=b'\xe5\x9c\xb0\xe5\x9d\x80', max_length=100)),
                ('opendate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe9\x96\x8b\xe6\xa5\xad\xe6\x97\xa5\xe6\x9c\x9f')),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': '\u5e97\u8216\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=b'\xe5\xa7\x93\xe5\x90\x8d', max_length=10)),
                ('sex', models.CharField(choices=[(b'F', b'\xe5\xa5\xb3\xe6\x80\xa7'), (b'M', b'\xe7\x94\xb7\xe6\x80\xa7')], default=b'F', help_text=b'\xe6\x80\xa7\xe5\x88\xab', max_length=2)),
                ('image', models.ImageField(blank=True, help_text=b'\xe7\x85\xa7\xe7\x89\x87', null=True, upload_to=b'staffs')),
                ('edu', models.CharField(help_text=b'\xe5\xad\xb8\xe6\xad\xb7', max_length=4)),
                ('marital', models.BooleanField(choices=[(True, b'\xe5\xb7\xb2\xe5\xa9\x9a'), (False, b'\xe6\x9c\xaa\xe5\xa9\x9a')], default=False, help_text=b'\xe5\xa9\x9a\xe5\x90\xa6')),
                ('school', models.CharField(blank=True, help_text=b'\xe7\x95\xa2\xe6\xa5\xad\xe5\xad\xb8\xe6\xa0\xa1', max_length=100, null=True)),
                ('graduation', models.DateField(blank=True, help_text=b'\xe7\x95\xa2\xe6\xa5\xad\xe6\x97\xa5\xe6\x9c\x9f', null=True)),
                ('address', models.CharField(help_text=b'\xe4\xbd\x8f\xe5\x9d\x80', max_length=100)),
                ('cellphone', models.CharField(help_text=b'\xe6\x89\x8b\xe6\xa9\x9f', max_length=11)),
                ('idcode', models.CharField(help_text=b'\xe8\xba\xab\xe4\xbb\xbd\xe8\xad\x89\xe8\x99\x9f', max_length=18, unique=True)),
                ('homephone', models.CharField(help_text=b'\xe7\xb7\x8a\xe6\x80\xa5\xe8\x81\xaf\xe7\xb9\xab\xe9\x9b\xbb\xe8\xa9\xb1', max_length=11)),
                ('level', models.SmallIntegerField(choices=[(1, b'\xe8\x91\xa3\xe4\xba\x8b'), (2, b'\xe6\x9c\x83\xe8\xa8\x88'), (3, b'\xe5\x80\x89\xe7\xae\xa1'), (4, b'\xe7\xb6\x93\xe7\x90\x86'), (5, b'\xe5\xba\x97\xe9\x95\xb7'), (6, b'\xe5\xba\x97\xe5\x93\xa1'), (7, b'\xe5\xbe\x8c\xe5\x8b\xa4'), (8, b'\xe5\xaf\xa6\xe7\xbf\x92'), (9, b'\xe5\x85\xb6\xe4\xbb\x96'), (99, b'\xe9\x9b\xa2\xe8\x81\xb7')], default=6, help_text=b'\xe8\x81\xb7\xe4\xbd\x8d')),
                ('joindate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\xb0\xe8\x81\xb7\xe6\x97\xa5\xe6\x9c\x9f')),
                ('exwork', models.CharField(blank=True, help_text=b'\xe5\xb7\xa5\xe4\xbd\x9c\xe7\xb6\x93\xe6\xad\xb7', max_length=255, null=True)),
                ('family', models.CharField(help_text=b'\xe5\xae\xb6\xe5\xba\xad\xe6\x88\x90\xe5\x93\xa1\xe5\x8f\x8a\xe9\x97\x9c\xe4\xbf\x82', max_length=255)),
                ('note', models.CharField(blank=True, help_text=b'\xe5\x82\x99\xe8\xa8\xbb', max_length=100, null=True)),
                ('shop', models.ManyToManyField(to='psi.Shop')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '\u4eba\u54e1\u7ba1\u7406',
            },
        ),
        migrations.AddField(
            model_name='sellorder',
            name='shop',
            field=models.ForeignKey(help_text=b'\xe5\xba\x97\xe9\x93\xba', on_delete=django.db.models.deletion.CASCADE, to='psi.Shop'),
        ),
        migrations.AddField(
            model_name='sellorder',
            name='staff',
            field=models.ForeignKey(help_text=b'\xe9\x94\x80\xe5\x94\xae\xe5\x91\x98\xe5\xb7\xa5', on_delete=django.db.models.deletion.CASCADE, to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='remit',
            name='staff',
            field=models.ForeignKey(help_text=b'\xe5\x8c\xaf\xe6\xac\xbe\xe4\xba\xba', on_delete=django.db.models.deletion.CASCADE, to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='payslip',
            name='staff',
            field=models.ForeignKey(help_text=b'\xe5\x93\xa1\xe5\xb7\xa5', on_delete=django.db.models.deletion.CASCADE, to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='outstream',
            name='keeper',
            field=models.ForeignKey(help_text=b'\xe4\xbb\x93\xe7\xae\xa1', on_delete=django.db.models.deletion.CASCADE, related_name='out_keeper_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='outstream',
            name='shop',
            field=models.ForeignKey(help_text=b'\xe6\x8f\x90\xe8\xb4\xa7\xe5\xba\x97\xe9\x93\xba', on_delete=django.db.models.deletion.CASCADE, to='psi.Shop'),
        ),
        migrations.AddField(
            model_name='outstream',
            name='staff1',
            field=models.ForeignKey(help_text=b'\xe6\x8f\x90\xe8\xb4\xa7\xe4\xba\xba\xe4\xb8\x80', on_delete=django.db.models.deletion.CASCADE, related_name='out_sells_1_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='outstream',
            name='staff2',
            field=models.ForeignKey(blank=True, help_text=b'\xe6\x8f\x90\xe8\xb4\xa7\xe4\xba\xba\xe4\xba\x8c', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_sells_2_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='outdetail',
            name='outid',
            field=models.ForeignKey(help_text=b'\xe5\x87\xba\xe5\xba\x93\xe5\x8d\x95ID', on_delete=django.db.models.deletion.CASCADE, to='psi.OutStream'),
        ),
        migrations.AddField(
            model_name='outdetail',
            name='product',
            field=models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', on_delete=django.db.models.deletion.CASCADE, to='psi.Products'),
        ),
        migrations.AddField(
            model_name='instream',
            name='keeper',
            field=models.ForeignKey(help_text=b'\xe5\x80\x89\xe7\xae\xa1', on_delete=django.db.models.deletion.CASCADE, related_name='in_keeper_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='instream',
            name='staff1',
            field=models.ForeignKey(help_text=b'\xe6\x94\xb6\xe8\xb2\xa8\xe4\xba\xba\xe4\xb8\x80', on_delete=django.db.models.deletion.CASCADE, related_name='in_sells_1_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='instream',
            name='staff2',
            field=models.ForeignKey(blank=True, help_text=b'\xe6\x94\xb6\xe8\xb2\xa8\xe4\xba\xba\xe4\xba\x8c', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_sells_2_set', to='psi.Staff'),
        ),
        migrations.AddField(
            model_name='indetail',
            name='inid',
            field=models.ForeignKey(help_text=b'\xe5\x85\xa5\xe5\xba\xab\xe5\x96\xaeID', on_delete=django.db.models.deletion.CASCADE, to='psi.InStream'),
        ),
        migrations.AddField(
            model_name='indetail',
            name='product',
            field=models.ForeignKey(help_text=b'\xe5\x95\x86\xe5\x93\x81', on_delete=django.db.models.deletion.CASCADE, to='psi.Products'),
        ),
        migrations.AddField(
            model_name='customer',
            name='shop',
            field=models.ForeignKey(help_text=b'\xe5\xba\x97\xe9\x93\xba', on_delete=django.db.models.deletion.CASCADE, to='psi.Shop'),
        ),
    ]
