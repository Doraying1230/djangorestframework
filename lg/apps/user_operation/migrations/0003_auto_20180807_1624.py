# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-07 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20180804_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userleavingmessage',
            old_name='mssage',
            new_name='message',
        ),
    ]