# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-29 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatportal', '0009_auto_20170123_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senateseat',
            name='swingseat',
            field=models.BooleanField(default=False, verbose_name='Is seat up for election in the next cycle?'),
        ),
    ]
