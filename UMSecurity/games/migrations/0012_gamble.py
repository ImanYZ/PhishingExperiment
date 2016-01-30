# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0011_auto_20160129_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gamble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen', models.IntegerField(default=0)),
                ('coin1', models.BooleanField(default=0)),
                ('coin2', models.BooleanField(default=0)),
                ('coin3', models.BooleanField(default=0)),
                ('coin4', models.BooleanField(default=0)),
                ('coin5', models.BooleanField(default=0)),
                ('coin6', models.BooleanField(default=0)),
                ('coin7', models.BooleanField(default=0)),
                ('coin8', models.BooleanField(default=0)),
                ('coin9', models.BooleanField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('originalPoints', models.IntegerField(default=0)),
                ('willingness', models.FloatField(default=0)),
                ('willingnessRand', models.FloatField(default=16)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.User')),
            ],
        ),
    ]
