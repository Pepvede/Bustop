# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bustopapp', '0009_auto_20170104_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linea',
            old_name='linea',
            new_name='numero',
        ),
    ]
