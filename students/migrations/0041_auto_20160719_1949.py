# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0040_auto_20160719_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='DOB',
            field=models.DateField(),
        ),
    ]