# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_info_shirt_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='info',
            old_name='Websites',
            new_name='Website',
        ),
        migrations.RemoveField(
            model_name='info',
            name='Test_Scores',
        ),
        migrations.RemoveField(
            model_name='info',
            name='shirt_size',
        ),
        migrations.AlterField(
            model_name='info',
            name='Course',
            field=models.CharField(choices=[('ipg', 'IPG'), ('mtech', 'MTECH'), ('mba', 'MBA'), ('phd', 'PHD')], default='ipg', max_length=10),
        ),
        migrations.AddField(
            model_name='info',
            name='Education',
            field=models.ManyToManyField(to='students.education', verbose_name='list of sites'),
        ),
    ]
