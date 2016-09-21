# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 00:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='FK_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_course', to='mycourses.Courses'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='FK_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classroom_student', to='loginapp.Users'),
        ),
    ]
