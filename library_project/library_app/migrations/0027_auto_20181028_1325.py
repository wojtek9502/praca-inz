# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 12:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0026_auto_20181028_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='receive_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 27, 13, 25, 37, 873696)),
        ),
    ]
