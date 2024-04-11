import datetime
from django.utils import timezone

from celery import shared_task

from BookingApp.models import Flight, Airport, Airline


@shared_task
def create_flight():
    bel_ap = Airport.objects.get(airport_name='Беларусь')
    mocs_ap = Airport.objects.get(airport_name='Домодедово')
    turk_ap = Airport.objects.get(airport_name='ТурецкийАэропорт')
    belavia = Airline.objects.get(airline_name='BelAvia')
    aviasales = Airline.objects.get(airline_name='AviaSales')
    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=9),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=12),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=9),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=12),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=9),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=12),
                          price=150,
                          available_seats=90
                          )

    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=11),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=14),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=11),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=14),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=11),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=14),
                          price=150,
                          available_seats=90
                          )

    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=13),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=16),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=13),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=16),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=13),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=16),
                          price=150,
                          available_seats=90
                          )

    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=15),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=18),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=15),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=18),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=15),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=18),
                          price=150,
                          available_seats=90
                          )

    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=18),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=21),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=18),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=21),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=18),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=21),
                          price=150,
                          available_seats=90
                          )

    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=20),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=23),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=20),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=23),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aviasales,
                          departure_airport=mocs_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=20),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=23),
                          price=150,
                          available_seats=90
                          )
