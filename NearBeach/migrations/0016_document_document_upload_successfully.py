# Generated by Django 4.2.7 on 2023-11-22 09:07

from django.db import migrations, models


def set_successfully_status(apps, schema_editor):
    Document = apps.get_model("NearBeach", "Document")

    Document.objects.all().update(
        document_upload_successfully=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("NearBeach", "0015_notification_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="document_upload_successfully",
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(set_successfully_status, migrations.RunPython.noop)
    ]
