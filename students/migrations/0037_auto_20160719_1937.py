# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 14:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0036_auto_20160719_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='DOB',
            field=models.DateField(default=datetime.date.today, verbose_name='DOB'),
        ),
    ]