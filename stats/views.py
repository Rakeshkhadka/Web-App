from rest_framework import viewsets, mixins
from .models import SourceData, WeatherSummary
from .serializers import SourceDataSerializer, WeatherSummarySerializer
from weather.permissions import TenResultsPagination
# Create your views here.


class SourceDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class =   SourceDataSerializer
    queryset = SourceData.objects.all()
    pagination_class = TenResultsPagination
    filterset_fields = ['station_id', 'weatherdate']
    

class WeatherSummaryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherSummary.objects.all()
    serializer_class = WeatherSummarySerializer
    pagination_class = TenResultsPagination
    filterset_fields = ['station_id', 'year']
    
    
    
    
    



