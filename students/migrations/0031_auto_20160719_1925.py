# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 13:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0030_info_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='DOB',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
