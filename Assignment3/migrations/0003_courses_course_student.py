# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assignment3', '0002_auto_20151229_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='course_student',
            field=models.ManyToManyField(to='Assignment3.Student'),
        ),
    ]