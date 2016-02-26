from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date, datetime
from django.core.validators import MinValueValidator

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Location(models.Model):
  location = models.CharField(max_length=10, unique=True)
  def __str__ (self):
    return self.location

@python_2_unicode_compatible  # only if you need to support Python 2
class Typ(models.Model):
  typ = models.CharField(max_length=25, unique=True)
  def __str__ (self):
    return self.typ

@python_2_unicode_compatible  # only if you need to support Python 2
class Time_between_replacement(models.Model):
  tbr = models.IntegerField(unique=True)
  def __str__ (self):
    return str(self.tbr)

@python_2_unicode_compatible  # only if you need to support Python 2
class Category(models.Model):
  category = models.CharField(max_length=15, unique=True)
  def __str__ (self):
    return self.category

@python_2_unicode_compatible  # only if you need to support Python 2
class Inventary(models.Model):
  typ       = models.ForeignKey(Typ,            verbose_name='Typ')
  location  = models.ForeignKey(Location,       verbose_name='Ort')
  tbr       = models.ForeignKey(Time_between_replacement, verbose_name='Nutzungsdauer')
  category  = models.ForeignKey(Category,       verbose_name='Kategorie')
  objectname = models.CharField(max_length=255, verbose_name='Bezeichnung')
  vendor_str = models.CharField(max_length=255, verbose_name='Herstelleridentifikation')
  amount    = models.IntegerField(default=1,  validators=[MinValueValidator(1)],   verbose_name='Anzahl')
  date_of_purchase = models.DateField(default=date.today, editable=True, verbose_name='Anschaffungsdatum')
  single_value =    models.DecimalField(max_digits=11, decimal_places=2, default=0, verbose_name='Einzepreis')
  total_value =     models.DecimalField(max_digits=11, decimal_places=2, default=0, verbose_name='Gesamtpreis')
  fair_value =      models.DecimalField(max_digits=11, decimal_places=2, default=0, verbose_name='Abschreibung')
  inventary_nr = models.CharField(max_length=255, default='-'+str(datetime.now().year)+'-', unique=False, verbose_name='Inventar Nr.')
  def __str__ (self):
    return self.objectname

