# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-01 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='goods/banner', verbose_name='轮播图片'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='goods',
            field=models.ForeignKey(help_text='商品', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='goods.Goods', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='image',
            field=models.ImageField(blank=True, help_text='图片', null=True, upload_to='goods/goodsimages/', verbose_name='图片'),
        ),
    ]
