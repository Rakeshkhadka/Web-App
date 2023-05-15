from django.core.management.base import BaseCommand
from stats.models import SourceData
import os
from glob import glob
import timeit
from datetime import datetime


class Command(BaseCommand):
    help = "Ingest data to the database"
    
    def handle(self, *args, **kwargs):
        start_time = timeit.default_timer()
        records_to_create = []
        for file in glob('E:/Django/Weather-app/wx_data2/*'):
            stationfile = os.path.basename(file)
            file_name = stationfile.split(".")
            # base_name, extension = os.path.splitext(stationfile)
            
            # station_id = base_name
            station_id = file_name[0]
            with open(file) as f:
                for line in f:
                    weather_date, low_temp, high_temp, precipitation = line.strip().split('\t')
                    mydict = {
                        'station_id': station_id,
                        'weatherdate': datetime.strptime(weather_date, '%Y%m%d').date(),
                        'low_temperature': low_temp.replace(" ", ""),
                        'high_temperature': high_temp.replace(" ", ""),
                        'precipitation': precipitation.replace(" ", "")
                    }
                    if not SourceData.objects.filter(
                        station_id = mydict['station_id'], 
                        weatherdate=mydict['weatherdate']
                    ).exists():
                        records_to_create.append(SourceData(**mydict))
                        # num_records+=1
        # print(f"Number of records ingested: {num_records}")
        num_records = len(records_to_create)
        SourceData.objects.bulk_create(records_to_create)
        print(f"Number of records ingested: {num_records}")
        end_time = timeit.default_timer()
        print("Execution time:", end_time - start_time, "seconds")