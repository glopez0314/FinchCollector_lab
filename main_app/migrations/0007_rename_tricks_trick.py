# Generated by Django 4.2.3 on 2023-08-04 16:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main_app", "0006_tricks_items"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tricks",
            new_name="Trick",
        ),
    ]