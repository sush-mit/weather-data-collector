# Generated by Django 3.2.9 on 2021-12-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Station', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='country',
            field=models.ForeignKey(default='Select a country', on_delete=django.db.models.deletion.DO_NOTHING, to='Station.countries'),
        ),
    ]