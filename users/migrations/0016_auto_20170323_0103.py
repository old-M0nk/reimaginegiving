# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20170323_0057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='project_id',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='project',
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.DeleteModel(
            name='Donor',
        ),
    ]
