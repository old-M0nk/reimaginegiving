# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-16 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_donation_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
