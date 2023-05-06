# Generated by Django 3.2.16 on 2022-12-24 00:21

from django.db import migrations
from django.db.models import Count


def deduplicate_reviews(apps, schema_editor):
    Review = apps.get_model("submission", "Review")
    dupes = (
        Review.objects.all()
        .values("submission", "user")
        .annotate(submission_count=Count("submission"))
        .filter(submission_count__gt=1)
    )
    for dupe in dupes:
        all_reviews = list(
            Review.objects.all().filter(
                user=dupe["user"], submission=dupe["submission"]
            )
        )
        all_reviews.sort(key=lambda r: len(r.text), reverse=True)
        for review in all_reviews[1:]:
            review.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0069_resource_links"),
    ]

    operations = [migrations.RunPython(deduplicate_reviews, migrations.RunPython.noop)]
