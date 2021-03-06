# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Course', models.CharField(max_length=100)),
                ('Roll', models.CharField(max_length=100)),
                ('Pic', models.ImageField(upload_to='')),
                ('Email', models.EmailField(max_length=250)),
                ('Websites', models.URLField(max_length=250)),
                ('About', models.CharField(max_length=10000)),
                ('Education', models.CharField(max_length=10000)),
                ('Experience', models.CharField(max_length=100000)),
                ('Test_Scores', models.CharField(max_length=250)),
                ('Projects', models.CharField(max_length=100000)),
                ('Honors_Awards', models.CharField(max_length=100000)),
                ('Courses', models.CharField(max_length=10000)),
                ('Skills', models.CharField(max_length=10000)),
                ('Interests', models.CharField(max_length=10000)),
            ],
        ),
    ]
