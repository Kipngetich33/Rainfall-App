# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rainfallapp', '0002_auto_20180506_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_rainfall',
            name='record_date',
            field=models.DateTimeField(null=True),
        ),
    ]
