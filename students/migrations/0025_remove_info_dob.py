# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_auto_20160716_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='DOB',
        ),
    ]
