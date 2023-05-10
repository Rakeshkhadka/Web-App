from django.shortcuts import render, HttpResponse
from .models import Weather_data

# Create your views here.

import os
from datetime import datetime
def create_weather_dates(request):
    y = '/home/intern2/Desktop/Aayulogic_Python/Web-App/wx_data'
    for file in os.listdir(y):
        if os.path.isfile(os.path.join(y, file)):
            print(os.path.join(y, file))
            with open(os.path.join(y, file)) as f:
                data_list=f.readlines()
                for datae in data_list:
                    my_data=list(datae.split('\t'))
                    mydict = {}
                    mydict['station_id'] = file.replace('.txt', '')
                    mydict['weatherdate'] = datetime.strptime(my_data[0], '%Y%m%d').date()
                    mydict['low_temperature'] = my_data[1].replace(" ", "")
                    mydict['high_temperature'] = my_data[2].replace(" ", "")
                    mydict['precipitation'] = my_data[3].replace(" ", "")
                    if not  Weather_data.objects.filter(weatherdate=mydict['weatherdate'], station_id=  mydict['station_id'],  low_temperature=mydict['low_temperature'], high_temperature=mydict['high_temperature'], precipitation=mydict['precipitation']).exists():
                        Weather_data.objects.create(**mydict)
    return HttpResponse("hello")