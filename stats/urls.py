from django.urls import path, include
from .views import SourceDataViewSet, WeatherSummaryViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'weather', SourceDataViewSet, basename='weather')
# router.register(r'weather/stats', WeatherSummaryViewset, basename='weather-summary')
urlpatterns = [
    path('weather/stats/', WeatherSummaryViewset.as_view({'get': 'list'}), name='weather-summary-list'),
    path('weather/stats/<int:pk>/', WeatherSummaryViewset.as_view({'get': 'retrieve'}), name='weather-summary-detail'),
    path('', include(router.urls)),
]