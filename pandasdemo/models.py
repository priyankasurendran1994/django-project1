from django.db import models

# Create your models here.

class data(models.Model):
   year = models.IntegerField(("year"),max_length=255)
   sex = models.CharField(("sex"),max_length=255)
   age_group = models.CharField(("age_group"),max_length=255)
   Geographic_region_where_injury_occurred = models.CharField(("Geographic_region_where_injury_occurred"),max_length=255)
   Employment_status = models.CharField(("Employment_status"),max_length=255)
   Occupation = models.CharField(("Occupation"),max_length=255)

