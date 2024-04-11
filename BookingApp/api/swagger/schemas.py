from drf_yasg.utils import swagger_auto_schema

from .. import serializers


flights_api_doc = swagger_auto_schema(
    responses={
        201: serializers.FlightSerializer(),
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
    }
)

airports_api_doc = swagger_auto_schema(
    responses={
        201: serializers.AirportSerializer(),
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server Error",
    }
)

airlines_api_doc = swagger_auto_schema(
    responses={
        201: serializers.AirlineSerializer(),
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Error",
    }
)

orders_api_doc = swagger_auto_schema(
    responses={
        201: serializers.OrderSerializer(),
        400: "Bad request",
        401: "Unauthorized",
        500: "Internal Error"
    }
)

reviews_api_doc = swagger_auto_schema(
    responses={
        201: serializers.ReviewSerializer(),
        400: "Bad Request",
        401: "Unauthorized",
        500: "Internal Server",
    }
)
