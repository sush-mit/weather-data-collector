# Generated by Django 3.2.9 on 2021-12-09 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Station", "0002_alter_station_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="station",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="Station.countries"
            ),
        ),
    ]
