# Generated by Django 1.11.7 on 2017-11-04 15:40

from django.db import migrations, models
import pretalx.submission.models.question


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0012_question_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="answer_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=pretalx.submission.models.question.answer_file_path,
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="variant",
            field=models.CharField(default="string", max_length=15),
        ),
    ]
