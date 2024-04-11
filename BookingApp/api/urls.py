from django.urls import path
from . import views


# /api/


app_name = 'posts:api'


urlpatterns = [
    path("flights", views.FlightListCreateAPIView.as_view(), name='flights-list-create'),
    path("flight/<int:pk>", views.FlightDetailAPIView.as_view(), name='flight'),
    path("airports", views.AirportListAPIView.as_view(), name='airports-list-create'),
    path("airport/<int:pk>", views.AirportDetailAPIView.as_view(), name='airport'),
    path("airlines", views.AirlineListAPIView.as_view(), name='airlines-list-create'),
    path("airline/<int:pk>", views.AirlineDetailAPIView.as_view(), name='airline'),
    path("orders", views.OrderListAPIView.as_view(), name='orders-list-create'),
    path("order/<int:pk>", views.OrderDetailAPIView.as_view(), name='order'),
    path("reviews", views.ReviewListAPIView.as_view(), name='reviews-list-create'),
    path("review/<int:pk>", views.ReviewDetailAPIView.as_view(), name='review'),
]
