# Generated by Django 2.0.2 on 2018-03-05 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("mail", "0003_auto_20171001_1358"),
        ("event", "0010_event_plugins"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="question_template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="mail.MailTemplate",
            ),
        ),
    ]
