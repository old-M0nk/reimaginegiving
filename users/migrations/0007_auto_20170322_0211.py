# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_donor_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='address_line_1',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='address_line_2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='mobile_number',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='occupation',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='pan_number',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='pincode',
            field=models.IntegerField(default=''),
        ),
    ]
