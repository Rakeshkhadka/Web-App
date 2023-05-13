from rest_framework import viewsets, mixins
from .models import SourceData, WeatherSummary
from .serializers import SourceDataSerializer, WeatherSummarySerializer
from weather.permissions import TenResultsPagination
# Create your views here.


class SourceDataListRetrieveViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class =   SourceDataSerializer
    queryset = SourceData.objects.all()
    pagination_class = TenResultsPagination
    
    
    
class SummaryDataListRetrieveViewset(mixins.ListModelMixin,
                                     mixins.RetrieveModelMixin,
                                     viewsets.GenericViewSet):
    serializer_class = WeatherSummarySerializer
    queryset = WeatherSummary.objects.all()
    pagination_class = TenResultsPagination
    
    
    
    
    
    
# import os
# from datetime import datetime
# from glob import glob
# def create_weather_dates(request): 
#     # num_records = 0
#     records_to_create = []
#     for file in glob('E:/Django/Weather-app/wx_data2/*'):
#         stationfile = os.path.basename(file)
#         base_name, extension = os.path.splitext(stationfile)
#         station_id = base_name
#         with open(file) as f:
#             for line in f:
#                 weather_date, low_temp, high_temp, precipitation = line.strip().split('\t')
#                 mydict = {
#                      'station_id': station_id,
#                      'weatherdate': datetime.strptime(weather_date, '%Y%m%d').date(),
#                      'low_temperature': low_temp.replace(" ", ""),
#                      'high_temperature': high_temp.replace(" ", ""),
#                      'precipitation': precipitation.replace(" ", "")
#                  }
#                 if not  Weather_data.objects.filter(station_id = mydict['station_id'], weatherdate=mydict['weatherdate']).exists():
#                     records_to_create.append(Weather_data(**mydict))
#                     # num_records+=1
#     # print(f"Number of records ingested: {num_records}")
#     num_records = len(records_to_create)
#     Weather_data.objects.bulk_create(records_to_create)
#     print(f"Number of records ingested: {num_records}")
#     return HttpResponse("hello")





# if os.path.isfile(os.path.join(y, file)):
#     print(os.path.join(y, file))
#     with open(os.path.join(y, file)) as f:
#         data_list=f.readlines()
#         for datae in data_list:
#             my_data=list(datae.split('\t'))
#             mydict = {}
#             mydict['station_id'] = file.replace('.txt', '')
#             mydict['weatherdate'] = datetime.strptime(my_data[0], '%Y%m%d').date()
#             mydict['low_temperature'] = my_data[1].replace(" ", "")
#             mydict['high_temperature'] = my_data[2].replace(" ", "")
#             mydict['precipitation'] = my_data[3].replace(" ", "")
  



