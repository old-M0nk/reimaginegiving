# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20170321_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelineevents',
            name='days_span',
            field=models.IntegerField(default=0),
        ),
    ]
