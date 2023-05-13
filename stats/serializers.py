from rest_framework import serializers
from .models import SourceData, WeatherSummary


class SourceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceData
        fields = '__all__'
        
        
class WeatherSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherSummary
        fields = '__all__'