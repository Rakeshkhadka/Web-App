from django.contrib import admin
from .models import Weather_data
# Register your models here.
# admin.site.register(Weather_data)

# class AuthorAdmin(admin.ModelAdmin):
    


@admin.register(Weather_data)
class Weather_dataAdmin(admin.ModelAdmin):
    list_display = ["weatherdate", "low_temperature", "high_temperature", "precipitation"]