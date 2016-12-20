# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 16:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0029_remove_info_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='DOB',
            field=models.DateField(auto_now=True, default=datetime.datetime(2016, 7, 16, 16, 27, 49, 736365, tzinfo=utc)),
            preserve_default=False,
        ),
    ]