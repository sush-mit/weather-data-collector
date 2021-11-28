import csv

from django.apps import AppConfig

from .csv_data import CSVData


class StationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Station"

    def ready(self):
        # with open('countries-states-cities-csv/states_data-redacted.csv', 'r') as states_csv:
        #   csv_reader = csv.DictReader(states_csv)
        #   for item in csv_reader:
        #     CSVData.STATES.append(dict(item))

        with open(
            "countries-states-cities-csv/cities_data-redacted.csv", "r"
        ) as cities_csv:
            csv_reader = csv.DictReader(cities_csv)
            for item in csv_reader:
                CSVData.CITIES.append(dict(item))
