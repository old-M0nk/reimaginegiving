# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-23 14:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0017_donation_donor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supported_projects_mobile', models.BooleanField(default=True)),
                ('supported_projects_email', models.BooleanField(default=True)),
                ('general_mobile', models.BooleanField(default=True)),
                ('general_email', models.BooleanField(default=True)),
                ('exciting_projects_mobile', models.BooleanField(default=True)),
                ('exciting_projects_email', models.BooleanField(default=True)),
                ('username', models.ForeignKey(on_delete=models.SET('team member not set'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
