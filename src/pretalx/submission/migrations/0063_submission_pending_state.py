# Generated by Django 3.2.10 on 2021-12-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0062_cfp_settings_data"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="pending_state",
            field=models.CharField(default=None, max_length=9, null=True),
        ),
    ]
