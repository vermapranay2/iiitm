# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20160708_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
