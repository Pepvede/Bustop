# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bustopapp', '0006_auto_20170103_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paradaseleccionada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=3)),
            ],
        ),
    ]
