# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-04 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20170305_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='project_page_desc',
            field=models.TextField(blank=True),
        ),
    ]
