# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-21 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingdata',
            name='avg_dem',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='democrat Polling Average'),
        ),
        migrations.AlterField(
            model_name='pollingdata',
            name='avg_gop',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='republican Polling Average'),
        ),
        migrations.AlterField(
            model_name='pollingdata',
            name='avg_ind',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, verbose_name='independent Polling Average (Can be NULL)'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='demographic_c',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='conservative Demographic'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='demographic_m',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='moderate Demographic'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='demographic_p',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='progressive Demographic'),
        ),
    ]