# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0028_info_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='DOB',
        ),
    ]