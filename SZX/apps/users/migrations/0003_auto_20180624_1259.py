# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-24 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_is_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(max_length=200, upload_to='banner/%y/%m', verbose_name='轮播图片'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(default='http://www.atguigu.com/', max_length=100, verbose_name='轮播图片链接'),
        ),
        migrations.AlterField(
            model_name='emailverify',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='emailverify',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '修改'), ('changeemail', '修改邮箱')], max_length=20, verbose_name='验证码类型'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='用户地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='用户生日'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('girl', '女'), ('boy', '男')], default='girl', max_length=5, verbose_name='用户性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/%y/%m', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='用户手机'),
        ),
    ]
