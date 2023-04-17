from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_airport = models.CharField(max_length=30)
    arrival_airport = models.CharField(max_length=30)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    company = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.flight_number} {self.departure_airport} - {self.arrival_airport} {self.departure_date} {self.departure_time}'


class Passenger(models.Model):
    TC_id_number = models.BigIntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(
        Flight, related_name="reservation", on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, related_name="reservations")

    def __str__(self):
        return f'{self.flight}'
