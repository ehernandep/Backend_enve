from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point
# Create your models here.


class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=150)
    energy_generation = models.DecimalField(max_digits=50, decimal_places=1)
    parking_places = models.DecimalField(max_digits=50, decimal_places=1)
    date_posted = models.DateTimeField(default=timezone.now)
    location = models.PointField(blank=True, null=True, srid=4326)
