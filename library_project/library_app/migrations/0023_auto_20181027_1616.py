# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 14:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0022_auto_20181027_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='receive_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 26, 16, 16, 16, 3160)),
        ),
    ]