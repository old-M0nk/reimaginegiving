# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-16 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_auto_20170416_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='status',
        ),
    ]
