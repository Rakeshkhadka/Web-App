from django.db import models
from decimal import Decimal
# Create your models here.


class SourceData(models.Model):
    station_id = models.CharField(max_length=255)
    weatherdate = models.DateField()
    low_temperature = models.IntegerField()
    high_temperature = models.IntegerField()
    precipitation = models.IntegerField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.weatherdate)

class WeatherSummary(models.Model):
    station_id   = models.CharField(max_length=255)
    year         = models.IntegerField()
    avg_max_temp = models.DecimalField(max_digits=10, decimal_places=2)
    avg_min_temp = models.DecimalField(max_digits=10, decimal_places=2)
    avg_precipitation  = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.avg_max_temp = Decimal(str(self.avg_max_temp))
        self.avg_min_temp = Decimal(str(self.avg_min_temp))
        self.avg_precipitation = Decimal(str(self.avg_precipitation))
        super().save(*args, **kwargs)
    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.weatherdate)


