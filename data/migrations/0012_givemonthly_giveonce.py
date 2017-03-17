# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-17 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20170315_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiveMonthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tag', models.TextField()),
                ('project_id', models.ForeignKey(on_delete=models.SET('project not set'), to='data.Project')),
            ],
        ),
        migrations.CreateModel(
            name='GiveOnce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tag', models.TextField()),
                ('project_id', models.ForeignKey(on_delete=models.SET('project not set'), to='data.Project')),
            ],
        ),
    ]