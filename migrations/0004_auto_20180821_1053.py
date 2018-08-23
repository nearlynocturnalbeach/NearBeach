# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 10:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0003_auto_20180816_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='quote_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user_groups',
            name='group_leader',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5),
        ),
        migrations.AddField(
            model_name='user_groups',
            name='reports_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_to', to=settings.AUTH_USER_MODEL),
        ),
    ]