from django.contrib.auth import get_user_model
from rest_framework import serializers
from BookingApp.models import Flight, Airline, Airport, Review, Order


# ================== USER =============================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


# ================== AIRPORT =============================
class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ["id", "airport_name", "city", "country", "latitude", "longitude"]
        read_only_fields = ["id"]
        write_only_fields = ["airport_name", "city", "country", "latitude", "longitude"]

    def create(self, validated_data):
        airport = Airport.objects.create(**validated_data)
        return airport


class AirportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ["id", "airport_name", "city", "country", "latitude", "longitude"]


# ================== AIRLINE =============================
class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ["id", "airline_name", "contact_info", "website"]
        read_only_fields = ["id"]
        write_only_fields = ["airline_name", "contact_info", "website"]

    def create(self, validated_data):
        airline = Airline.objects.create(**validated_data)
        return airline


class AirlineListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ["id", "airline_name", "contact_info", "website"]


# ================== FLIGHT =============================
class FlightSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()

    class Meta:
        model = Flight
        fields = ["id", "departure_date_time", "arrival_date_time", "price", "available_seats", "airline",
                  "departure_airport", "arrival_airport"]
        read_only_fields = ["id",]
        write_only_fields = ["departure_date_time", "arrival_date_time", "price", "available_seats", "airline",
                             "departure_airport", "arrival_airport"]

    def create(self, validated_data) -> Flight:
        flight = Flight.objects.create(**validated_data)
        return flight


class FlightListSerializer(serializers.ModelSerializer):
    airline = AirlineSerializer()
    departure_airport = AirportSerializer()
    arrival_airport = AirportSerializer()

    class Meta:
        model = Flight
        fields = ["id", "departure_date_time", "arrival_date_time", "price", "available_seats", "airline",
                  "departure_airport", "arrival_airport"]


# ================== ORDER =============================
class OrderSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ["id", "flight", "user", "seats_booked", "total_price", "booking_date_time"]
        read_only_fields = ["id", "flight", "user", ]

    def create(self, validated_data) -> Order:
        order = Order.objects.create(**validated_data)
        return order


class OrderListSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ["id", "flight", "user", "seats_booked", "total_price", "booking_date_time"]


# ================== REVIEW =============================
class ReviewSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ["id", "flight", "user", "rating", "comment"]
        read_only_fields = ["id", "flight", "user"]

    def create(self, validated_data) -> Review:
        review = Review.objects.create(**validated_data)
        return review


class ReviewListSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ["id", "flight", "user", "rating", "comment"]