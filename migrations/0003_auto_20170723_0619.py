# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 06:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0002_initialise_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='opportunity_expected_close_date',
            field=models.DateTimeField(),
        ),
    ]
