# Generated by Django 5.0.2 on 2024-02-10 20:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("reservations", "0001_initial"),
        ("users", "0004_profile_profile_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("description", models.CharField(max_length=360)),
                (
                    "rate",
                    models.PositiveIntegerField(
                        choices=[
                            (1, "Bad"),
                            (2, "Poor"),
                            (3, "Nice"),
                            (4, "Good"),
                            (5, "Perfect"),
                        ],
                        default=3,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "profile",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.profile",
                    ),
                ),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservations.reservation",
                    ),
                ),
            ],
        ),
    ]