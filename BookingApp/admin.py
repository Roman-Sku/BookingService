from django.contrib import admin
from .models import Flight, Airline, Airport, User, Review, Order

admin.site.register(Flight)
admin.site.register(Review)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(User)
admin.site.register(Order)
