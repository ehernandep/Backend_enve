from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an Email")
        if not password:
            raise ValueError("User must have an Password")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("User must have an Email")
        if not password:
            raise ValueError("User must have an Password")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    is_agent = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()


class Listing(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    borough = models.CharField(max_length=50, blank=True, null=True)
    choices_listing_type = (
        ("House", "House"),
        ("Apartment", "Apartment"),
        ("Office", "Office"),
    )
    listing_type = models.CharField(max_length=20, choices=choices_listing_type)

    choices_property_status = (("Sale", "Sale"), ("Rent", "Rent"))
    property_status = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_property_status
    )
    price = models.DecimalField(max_digits=100, decimal_places=0)
    choices_rental_frequency = (("Month", "Month"), ("Week", "Week"), ("Day", "Day"))
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequency
    )
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    location = models.PointField(blank=True, null=True, srid=4326)

    def __str__(self):
        return self.title
