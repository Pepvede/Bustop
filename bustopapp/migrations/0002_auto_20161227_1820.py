# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bustopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Gps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='bus',
            name='posiciongm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustopapp.Gm'),
        ),
        migrations.AlterField(
            model_name='bus',
            name='posiciongps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustopapp.Gps'),
        ),
    ]