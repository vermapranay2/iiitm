# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0044_auto_20160719_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='DOB',
        ),
    ]
