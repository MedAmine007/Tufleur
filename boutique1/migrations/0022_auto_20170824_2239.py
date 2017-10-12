# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 22:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique1', '0021_auto_20170824_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 22, 39, 15, 561576)),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 22, 39, 15, 563804)),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 22, 39, 15, 563887)),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 22, 39, 15, 563862)),
        ),
        migrations.AlterField(
            model_name='shop',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 22, 39, 15, 556724)),
        ),
    ]