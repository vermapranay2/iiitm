# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0046_auto_20160719_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Pic',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
