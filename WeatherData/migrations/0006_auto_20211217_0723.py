# Generated by Django 3.2.9 on 2021-12-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("WeatherData", "0005_auto_20211217_0640"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="weatherdata",
            name="date",
        ),
        migrations.RemoveField(
            model_name="weatherdata",
            name="time",
        ),
        migrations.AddField(
            model_name="weatherdata",
            name="date_time",
            field=models.DateTimeField(null=True),
        ),
    ]
