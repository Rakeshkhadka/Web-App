from django.contrib import admin
from .models import SourceData, WeatherSummary
# Register your models here.
# admin.site.register(MyModel)

# class AuthorAdmin(admin.ModelAdmin):
    


@admin.register(SourceData)
class SourceDataAdmin(admin.ModelAdmin):
    list_display = ["weatherdate", "station_id", "high_temperature", "low_temperature", "precipitation"]
    list_display_links = ('weatherdate', 'station_id')
    list_filter = ["weatherdate", "station_id"]
    
@admin.register(WeatherSummary)
class WeatherSummaryAdmin(admin.ModelAdmin):
    list_display = ["station_id", "year", "avg_max_temp", "avg_min_temp", "avg_precipitation"]
    list_display_links = ('year', 'station_id')