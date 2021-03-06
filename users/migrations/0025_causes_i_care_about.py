# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 11:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0025_gallerypic'),
        ('users', '0024_auto_20170331_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Causes_I_Care_About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Cause')),
                ('username', models.ForeignKey(on_delete=models.SET('team member not set'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
