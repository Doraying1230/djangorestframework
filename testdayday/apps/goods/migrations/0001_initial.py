# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 18:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5546\u54c1\u7c7b\u522b')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u7c7b\u522b\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u522b\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=30, unique=True, verbose_name='\u5546\u54c1\u7f16\u53f7')),
                ('goos_name', models.CharField(max_length=30, unique=True, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('goods_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u5546\u54c1\u4ef7\u683c')),
                ('goods_image', models.ImageField(blank=True, null=True, upload_to='goods/%y/%m/%d', verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('goods_desc', models.CharField(max_length=500, verbose_name='\u5546\u54c1\u63cf\u8ff0')),
                ('goods_num', models.IntegerField(default=0, verbose_name='\u5546\u54c1\u5e93\u5b58')),
                ('goos_unit', models.CharField(max_length=10, verbose_name='\u5546\u54c1\u5355\u4f4d')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category', verbose_name='\u6240\u5c5e\u7c7b\u522b')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',
            },
        ),
    ]