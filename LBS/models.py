from django.db import models


class Facilities_Nairobi(models.Model):
    facility_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.facility_name
    
class Schools_Nairobi(models.Model):
    school_name =models.CharField(max_length=250)
    latitude =models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.school_name
    



# Create your models here.
