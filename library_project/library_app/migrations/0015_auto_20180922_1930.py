# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 17:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0014_auto_20180922_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]