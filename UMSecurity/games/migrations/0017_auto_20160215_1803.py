# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_auto_20160214_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamble',
            name='originalPoints',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='gamble',
            name='points',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='holtlaury',
            name='originalPoints',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='holtlaury',
            name='points',
            field=models.FloatField(default=0),
        ),
    ]
