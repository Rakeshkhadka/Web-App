from stats.models import SourceData, WeatherSummary
from django.core.management.base import BaseCommand
from django.db.models import  Avg, Q
import timeit



class Command(BaseCommand):
    help = 'Create Weather Summary based for every station for every year'

    def handle(self, *args, **kwargs):
        start_time = timeit.default_timer()
        sourcedata=SourceData.objects.values(
            'station_id', 'weatherdate__year'
            ).exclude(
                Q(high_temperature=-9999) | 
                Q(low_temperature=-9999) | 
                Q(precipitation=-9999)
            ).annotate(
                avg_max_temp=Avg('high_temperature'), 
                avg_min_temp=Avg('low_temperature'), 
                avg_precipitation=Avg('precipitation')
            )     
        weather_summaries = []   
        for data in sourcedata:
            if not WeatherSummary.objects.filter(
                station_id= data['station_id'], 
                year=data['weatherdate__year']
            ).exists():
                summary = WeatherSummary(
                    station_id = data.get('station_id', None),
                    year = data.get('weatherdate__year', None),
                    avg_max_temp = data.get('avg_max_temp', None),
                    avg_min_temp = data.get('avg_min_temp', None),
                    avg_precipitation = data.get('avg_precipitation', None)
                )
                weather_summaries.append(summary)
        WeatherSummary.objects.bulk_create(weather_summaries)
        end_time = timeit.default_timer()
        print("Execution time:", end_time - start_time, "seconds")