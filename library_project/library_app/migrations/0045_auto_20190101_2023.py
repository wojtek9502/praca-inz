# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-01 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0044_auto_20181204_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateField(verbose_name='Data wypożyczenia'),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='receive_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 2, 20, 23, 26, 258978), verbose_name='Data oddania'),
        ),
    ]
