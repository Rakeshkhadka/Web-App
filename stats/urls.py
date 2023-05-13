from django.urls import path, include
from .views import SourceDataListRetrieveViewSet, SummaryDataListRetrieveViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'weather', SourceDataListRetrieveViewSet, basename='weather')
# router.register(r'stats', SummaryDataListRetrieveViewset, basename="weathersummary")
router.register(r'stats', SummaryDataListRetrieveViewset, basename='weathersummary')
# router.register(r'sourcedata', CreateListRetrieveViewSet, basename='sourcedata')
urlpatterns = [
    # path('', views.create_weather_dates)
    path('', include(router.urls)),
]