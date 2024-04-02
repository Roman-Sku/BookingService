import pathlib

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Airport(models.Model):
    airport_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        db_table = 'airports'


class Airline(models.Model):
    airline_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'airlines'


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)
    adress = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'users'


class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport_id')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport_id')
    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()

    class Meta:
        db_table = 'flights'
        ordering = ['-departure_date_time']


class Order(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date_time = models.DateTimeField()

    class Meta:
        db_table = 'orders'


class Review(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        db_table = 'reviews'
