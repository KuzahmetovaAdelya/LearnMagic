# Generated by Django 4.2.13 on 2024-06-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_rename_users_persons"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
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
                (
                    "gameName",
                    models.CharField(
                        default="", max_length=50, verbose_name="Название"
                    ),
                ),
                (
                    "answer",
                    models.CharField(default="1", max_length=100, verbose_name="Ответ"),
                ),
            ],
        ),
    ]
