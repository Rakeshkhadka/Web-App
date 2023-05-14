from django.urls import path, include
from .views import SourceDataViewSet, WeatherSummaryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'weather', SourceDataViewSet, basename='weather')
router.register(r'weathers/stats', WeatherSummaryViewset, basename='weather-summary')
urlpatterns = [
    path('', include(router.urls)),
]