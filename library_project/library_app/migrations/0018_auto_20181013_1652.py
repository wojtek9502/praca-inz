# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0017_auto_20181013_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcopy',
            name='is_borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='receive_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 12, 16, 52, 3, 770978)),
        ),
    ]
