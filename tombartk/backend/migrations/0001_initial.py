# Generated by Django 4.2.7 on 2024-01-20 14:19

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields
import django_bleach.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("subtitle", django_bleach.models.BleachField()),
                ("description", django_bleach.models.BleachField()),
                (
                    "tags",
                    django_better_admin_arrayfield.models.fields.ArrayField(
                        base_field=models.CharField(max_length=64), size=None
                    ),
                ),
                ("repo_url", models.URLField()),
                ("website", models.URLField()),
                ("logo_url", models.URLField(blank=True, default=None, null=True)),
            ],
        ),
    ]
