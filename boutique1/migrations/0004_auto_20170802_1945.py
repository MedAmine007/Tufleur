# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boutique1', '0003_auto_20170801_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercant',
            name='commercant_type',
            field=models.CharField(blank=True, choices=[('PA', 'particulier'), ('SO', 'Societe')], max_length=20),
        ),
        migrations.AddField(
            model_name='commercant',
            name='description',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
