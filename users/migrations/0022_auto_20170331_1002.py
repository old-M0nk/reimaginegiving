# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-31 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20170331_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_details',
            name='card_holder',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='card_details',
            name='cvv',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card_details',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]
