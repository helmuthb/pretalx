# Generated by Django 3.2.16 on 2022-11-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mail", "0009_queuedmail_locale"),
    ]

    operations = [
        migrations.AddField(
            model_name="queuedmail",
            name="attachments",
            field=models.JSONField(default=None, null=True),
        ),
    ]
