from django.db import models

# Create your models here.


class Weather_data(models.Model):
    station_id = models.CharField(max_length=255)
    weatherdate = models.DateField()
    low_temperature = models.IntegerField()
    high_temperature = models.IntegerField()
    precipitation = models.IntegerField()

    class Meta:
        ordering = ("weatherdate",)

    def __str__(self):
        return str(self.weatherdate)
# for index, file in enumerate(os.listdir(y)):
#     ...:     if os.path.isfile(os.path.join(y, file)):
#     ...:         if index==0:
#     ...:             print(os.path.join(y, file))
#     ...:             with open(os.path.join(y, file)) as f:
#     ...:                 data_list=list(f.readline().strip().split('\t'))
#     ...:                 print(data_list)
#     ...:                 mydict = {}
#     ...:                 mydict['weatherdate'] = datetime.strptime(data_list[0], '%Y%m%d').date()
#     ...:                 mydict['low_temperature'] = my_data[1]
#     ...:                 mydict['high_temperature'] = my_data[2]
#     ...:                 mydict['precipitation'] = my_data[3]
#     ...:                 Weather_data.objects.create(**mydict)


#  for index, file in enumerate(os.listdir(y)):
#    ...:     if os.path.isfile(os.path.join(y, file)):
#    ...:         if index==0:
#    ...:             print(os.path.join(y, file))
#    ...:             with open(os.path.join(y, file)) as f:
#    ...:                 data_list=f.readlines()
#    ...:                 for datae in data_list:
#    ...:                     print(list(datae.split('\t')))


# if os.path.isfile(os.path.join(y, file)):
#     ...:         if index==0:
#     ...:             print(os.path.join(y, file))
#     ...:             with open(os.path.join(y, file)) as f:
#     ...:                 data_list=f.readlines()
#     ...:                 for datae in data_list:
#     ...:                     my_data=list(datae.strip().split('\t'))
#     ...:                     mydict = {}
#     ...:                     mydict['weatherdate'] = datetime.strptime(my_data[0], '%Y%m%d').date()
#     ...:                     mydict['low_temperature'] = my_data[1].replace(" ", "")
#     ...:                     mydict['high_temperature'] = my_data[2].replace(" ", "")
#     ...:                     mydict['precipitation'] = my_data[3].replace(" ", "")
#     ...:                     Weather_data.objects.create(**mydict)




# for index, file in enumerate(os.listdir(y)):
#     ...:     if os.path.isfile(os.path.join(y, file)):
#     ...:         if index==0:
#     ...:             print(os.path.join(y, file))
#     ...:             with open(os.path.join(y, file)) as f:
#     ...:                 data_list=f.readlines()
#     ...:                 for datae in data_list:
#     ...:                     my_data=list(datae.strip().split('\t'))
#     ...:                     mydict = {}
#     ...:                     mydict['weatherdate'] = datetime.strptime(my_data[0], '%Y%m%d').date()
#     ...:                     mydict['low_temperature'] = my_data[1].replace(" ", "")
#     ...:                     mydict['high_temperature'] = my_data[2].replace(" ", "")
#     ...:                     mydict['precipitation'] = my_data[3].replace(" ", "")
#     ...:                     Weather_data.objects.create(**mydict)