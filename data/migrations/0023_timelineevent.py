# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-21 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_delete_timelineevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('heading', models.TextField()),
                ('desc', models.TextField(blank=True)),
                ('days_span', models.IntegerField(default=0)),
                ('project_id', models.ForeignKey(on_delete=models.SET('project not set'), to='data.Project')),
            ],
        ),
    ]
