# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_remove_project_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='banner',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.TextField(blank=True),
        ),
    ]
