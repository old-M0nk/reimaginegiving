# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 17:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_timelineevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelineevent',
            name='project_id',
        ),
        migrations.DeleteModel(
            name='TimelineEvent',
        ),
    ]
