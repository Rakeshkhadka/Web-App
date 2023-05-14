import random
from datetime import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase



from .models import WeatherSummary, SourceData
from .serializers import WeatherSummarySerializer, SourceDataSerializer


# Create your tests here.       

from decimal import Decimal  
class SourceDataTestCase(APITestCase):
    def setUp(self):
        self.source_data_1 = SourceData.objects.create(
            station_id='1001', weatherdate='2022-01-01', high_temperature=25.0, low_temperature=15.0, precipitation=6
        )
        self.source_data_2 = SourceData.objects.create(
            station_id='1002', weatherdate='2022-01-02',  high_temperature=20.0, low_temperature=10.0, precipitation=16
        ) 
    
    def test_summaryedatalist(self):
        url = reverse('weather-list')
        response = self.client.get(url)
        source_data = SourceData.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
    def test_retrieve(self):
        url = reverse('weather-detail', kwargs={'pk': self.source_data_1.pk})
        response = self.client.get(url)
        serializer = SourceDataSerializer(self.source_data_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        
class WeatherSummaryTestCase(APITestCase):
    def setUp(self):
        self.source_data_1 = WeatherSummary.objects.create(
            station_id='1001', year=2022, avg_max_temp=25.0, avg_min_temp=15.0, avg_precipitation=6
        )
        self.source_data_2 =  WeatherSummary.objects.create(
            station_id='1001', year=2023, avg_max_temp=20.0, avg_min_temp=5.0, avg_precipitation=2
        )
    
    def test_summaryedatalist(self):
        url = reverse('weather-summary-list')
        response = self.client.get(url)
        source_data = WeatherSummary.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # serializer = WeatherSummarySerializer(source_data, many=True)
        # self.assertEqual(response.data, serializer.data)
        
        
    def test_retrieve(self):
        url = reverse('weather-summary-detail', kwargs={'pk': self.source_data_1.pk})
        response = self.client.get(url)
        serializer = WeatherSummarySerializer(self.source_data_1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)