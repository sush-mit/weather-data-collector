# Generated by Django 3.2.9 on 2021-12-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeatherData', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='cloud',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='date_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='humidity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='temperature_c',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='temperature_f',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='weather_condition',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
