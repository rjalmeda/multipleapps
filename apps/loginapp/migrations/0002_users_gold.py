# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='gold',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
