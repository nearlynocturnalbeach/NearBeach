# Generated by Django 4.1.4 on 2023-03-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NearBeach", "0005_kanbancard_kanban_card_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="objectassignment",
            name="link_relationship",
            field=models.CharField(
                choices=[
                    ("Block", "Block"),
                    ("Duplicate", "Duplicate"),
                    ("Relate", "Relate"),
                ],
                default="Relate",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="objectassignment",
            name="parent_link",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]