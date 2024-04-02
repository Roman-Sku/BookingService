from django.contrib import admin
from django.db.models import QuerySet, F
from django.db.models.functions import Upper
from .models import Flight, Airline, Airport, User, Review, Order
from django.utils.safestring import mark_safe


# @admin.register(Flights)
# class FlightsAdmin(admin.ModelAdmin):
#     list_display = ['airline', 'departure_airport', 'arrival_airport', 'departure_date_time',
#                     'arrival_date_time', 'price', 'available_seats']
#     search_fields = ['airline_id']
#     date_hierarchy = 'price'
# #    actions = ['']
# #    readonly_fields = ['']
#     fieldsets = (
#
#         (None, {'fields': ('airline', 'departure_airport', 'arrival_airport', 'departure_date_time',
#                            'arrival_date_time')}),
#         (None, {'fields': ('price', 'available_seats')})
#     )
#
# #    @admin.action(description='Create')
# #    def create_flight(self, request, queryset):

admin.site.register(Flight)
admin.site.register(Review)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(User)
admin.site.register(Order)
