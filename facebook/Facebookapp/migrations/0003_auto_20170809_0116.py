# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facebookapp', '0002_auto_20170807_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_final',
            old_name='user',
            new_name='profile',
        ),
        migrations.AlterField(
            model_name='profile_final',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
