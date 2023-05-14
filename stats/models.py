from django.db import models
from decimal import Decimal
# Create your models here.

#models for ingested data
class CommonModel(models.Model):
    station_id = models.CharField(max_length=255)
    
    class Meta:
        abstract = True
class SourceData(CommonModel):
    weatherdate = models.DateField()
    low_temperature = models.IntegerField()
    high_temperature = models.IntegerField()
    precipitation = models.IntegerField()

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return str(self.weatherdate)


#models for summary of weather for every year for every station
class WeatherSummary(CommonModel):
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
        return str(f'{"station id:" + self.station_id + " " + "| year:" + str(self.year)}')
