# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-19 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190219_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderperson',
            name='order_name',
            field=models.CharField(default='무명', max_length=6),
        ),
    ]
