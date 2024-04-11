from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from BookingApp.api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from BookingApp.api import serializers
from BookingApp.api.swagger.schemas import flights_api_doc, airports_api_doc, airlines_api_doc, orders_api_doc, reviews_api_doc
from BookingApp.models import Flight, Airline, Airport, Review, Order


# ==================== FLIGHT ========================
class FlightListCreateAPIView(ListCreateAPIView):
    queryset = Flight.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['@arrival_country', '@departure_country']
    ordering_fields = ['departure_date_time', 'price']
    pagination_class = PageNumberPagination

    @flights_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.FlightSerializer
        return serializers.FlightListSerializer


class FlightDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


# ==================== AIRPORT ========================
class AirportListAPIView(ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['airport_name', 'country']
    pagination_class = PageNumberPagination

    @airports_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AirportSerializer
        return serializers.AirportListSerializer


class AirportDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = serializers.AirportSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


# ==================== AIRLINE ========================
class AirlineListAPIView(ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['airline_name', 'contact_info']
    pagination_class = PageNumberPagination

    @airlines_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AirlineSerializer
        return serializers.AirlineListSerializer


class AirlineDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Airline.objects.all()
    serializer_class = serializers.AirlineListSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


# ==================== ORDER ========================
class OrderListAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user', 'flight']
    ordering_fields = ['seats_booked', 'booking_date_time']
    pagination_class = PageNumberPagination

    @orders_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.OrderSerializer
        return serializers.OrderListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsOwnerOrReadOnly]


# ==================== REVIEW ========================
class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = [IsAdminOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['flight', 'user']
    ordering_fields = ['rating']
    pagination_class = PageNumberPagination

    @reviews_api_doc
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.ReviewSerializer
        return serializers.ReviewListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewListSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    permission_classes = [IsOwnerOrReadOnly]
