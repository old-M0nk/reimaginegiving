# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170322_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
    ]
