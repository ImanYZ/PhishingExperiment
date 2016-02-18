# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 10:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_gamble'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invested', models.IntegerField(default=0)),
                ('otherreturned', models.IntegerField(default=0)),
                ('returned1', models.IntegerField(default=0)),
                ('returned2', models.IntegerField(default=0)),
                ('returned3', models.IntegerField(default=0)),
                ('returned4', models.IntegerField(default=0)),
                ('returned5', models.IntegerField(default=0)),
                ('returned6', models.IntegerField(default=0)),
                ('returned7', models.IntegerField(default=0)),
                ('returned8', models.IntegerField(default=0)),
                ('returned9', models.IntegerField(default=0)),
                ('returned10', models.IntegerField(default=0)),
                ('investmentpoints', models.IntegerField(default=0)),
                ('returnpoints', models.IntegerField(default=0)),
                ('started', models.DateTimeField(default=django.utils.timezone.now)),
                ('finished', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.User')),
            ],
        ),
    ]