import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from LBS.models import Schools_Nairobi


class Command(BaseCommand):
    help = 'Load data from Schools_Nairobi file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'Data' / 'Schools_Nairobi.csv'
        keys = ('school_name', 'Long','Lat')  # the CSV columns we will gather data from.
        
        records = []
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append({k: row[k] for k in keys})

        # extract the latitude and longitude from the Point object
        for record in records:
            longitude = float(record['Long'])
            latitude = float(record['Lat'])
            record['longitude'] = longitude
            record['latitude'] = latitude

        # for record in records:
        #     longitude, latitude = record['Long'],['Lat']
        #     record['longitude'] = float(longitude)
        #     record['latitude'] = float(latitude)

            # add the data to the database
            Schools_Nairobi.objects.get_or_create(
                school_name=record['school_name'],
                latitude=record['latitude'],
                longitude=record['longitude']
            )