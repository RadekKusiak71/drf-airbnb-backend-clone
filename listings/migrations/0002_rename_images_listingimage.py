# Generated by Django 5.0.2 on 2024-02-08 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Images",
            new_name="ListingImage",
        ),
    ]