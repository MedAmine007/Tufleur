# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique1', '0014_auto_20170807_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 7, 9, 51, 38, 990563)),
        ),
    ]
