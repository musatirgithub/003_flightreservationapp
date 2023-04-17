from django.contrib import admin
from .models import Reservation, Passenger, Flight

# Register your models here.
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Reservation)
