import datetime
from django.utils import timezone

from celery import shared_task

from BookingApp.models import Flight, Airport, Airline


@shared_task
def create_flight():
    bel_ap, _ = Airport.objects.get_or_create(airport_name='НАМ', city='Минск', country='Беларусь', latitude=0.0000001, longitude=0.000001)
    mosc_ap, _ = Airport.objects.get_or_create(airport_name='Домодедово', city='Москва', country='Россия', latitude=0.0000001, longitude=0.000001)
    turk_ap, _ = Airport.objects.get_or_create(airport_name='Эсенбога', city='Анкара', country='Турция', latitude=0.0000011, longitude=0.00000111)
    belavia, _ = Airline.objects.get_or_create(airline_name='BelAvia', contact_info='+375 (17) 220-25-55', website='www.belavia.com' )
    aeroflot, _ = Airline.objects.get_or_create(airline_name='АэроФлот', contact_info='+7 (495) 223-55-55', website='https://www.aeroflot.ru/us-ru' )
    Flight.objects.create(airline=belavia,
                          departure_airport=bel_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=9),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=12),
                          price=110,
                          available_seats=100
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=9),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=12),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
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
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=11),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=14),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
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
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=13),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=16),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
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
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=15),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=18),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
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
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=18),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=21),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
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
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=bel_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=20),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=23),
                          price=105,
                          available_seats=102
                          )
    Flight.objects.create(airline=aeroflot,
                          departure_airport=mosc_ap,
                          arrival_airport=turk_ap,
                          departure_date_time=timezone.now() + datetime.timedelta(hours=20),
                          arrival_date_time=timezone.now() + datetime.timedelta(hours=23),
                          price=150,
                          available_seats=90
                          )
