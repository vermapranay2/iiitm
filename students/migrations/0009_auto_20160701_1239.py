# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20160701_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='Test_Scores',
            field=models.CharField(max_length=1000),
        ),
    ]
