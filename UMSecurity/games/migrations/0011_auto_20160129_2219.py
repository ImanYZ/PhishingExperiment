# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 03:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_gamble'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamble',
            name='user',
        ),
        migrations.DeleteModel(
            name='Gamble',
        ),
    ]