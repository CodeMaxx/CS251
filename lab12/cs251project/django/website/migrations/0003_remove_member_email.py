# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20161025_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
    ]
