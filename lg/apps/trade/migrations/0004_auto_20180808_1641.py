# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 16:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20180807_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='trade_sn',
            new_name='trade_no',
        ),
    ]
