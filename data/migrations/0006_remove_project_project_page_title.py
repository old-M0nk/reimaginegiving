# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 05:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_ngo_project_page_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_page_title',
        ),
    ]
