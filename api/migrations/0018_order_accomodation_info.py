# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-15 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20170315_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accomodation_info',
            field=models.BooleanField(default=False, verbose_name='Send extra info about accomodation'),
        ),
    ]
