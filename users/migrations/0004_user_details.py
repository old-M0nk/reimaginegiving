# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-10 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20170306_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField()),
                ('pan_number', models.TextField()),
                ('occupation', models.TextField()),
                ('address_line_1', models.TextField()),
                ('address_line_2', models.TextField()),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=models.SET('team member not set'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
