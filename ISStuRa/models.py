from django.db import models

# Create your models here.
class Location(models.Model):
  location = models.CharField(max_length=10)

class Typ(models.Model):
  typ = models.CharField(max_length=25)

class Time_between_replacement(models.Model):
  tbr = models.IntegerField()

class Category(models.Model):
  category = models.CharField(max_length=15)

class Inventary(models.Model):
  typ = models.ForeignKey(Typ)
  location = models.ForeignKey(Location)
  tbr = models.ForeignKey(Time_between_replacement)
  category = models.ForeignKey(Category)
  objectname = models.CharField(max_length=255)
  vendor_str = models.CharField(max_length=255)
  amount = models.IntegerField(default=0)
  date_of_purchase = models.DateField(auto_now=True)
  single_value =    models.DecimalField(max_digits=11, decimal_places=2)
  total_value =     models.DecimalField(max_digits=11, decimal_places=2)
  fair_value =      models.DecimalField(max_digits=11, decimal_places=2)

