# Generated by Django 4.1.5 on 2023-01-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="pseudonym",
            field=models.CharField(blank=True, max_length=63, null=True),
        ),
    ]
