# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_orderdash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='good_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='orderperson',
            name='order_phone',
            field=models.CharField(max_length=20),
        ),
    ]