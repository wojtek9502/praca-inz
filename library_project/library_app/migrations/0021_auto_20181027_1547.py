# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-27 13:47
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0020_auto_20181027_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='receive_date',
            field=models.DateField(default=datetime.datetime(2018, 12, 26, 15, 47, 14, 163122)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='receive_librarian',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receive_librarian', to=settings.AUTH_USER_MODEL),
        ),
    ]