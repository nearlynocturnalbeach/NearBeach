# Generated by Django 5.0.3 on 2024-05-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NearBeach", "0027_userjob"),
    ]

    operations = [
        migrations.AddField(
            model_name="userjob",
            name="job_sort_number",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
