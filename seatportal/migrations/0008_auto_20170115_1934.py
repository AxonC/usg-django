# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-15 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seatportal', '0007_remove_senateseat_demo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='senateseat',
            name='user',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='username of Player'),
        ),
    ]
