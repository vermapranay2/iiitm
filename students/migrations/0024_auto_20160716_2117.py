# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0023_auto_20160716_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='DOB',
            field=models.DateField(auto_now=True),
        ),
    ]
