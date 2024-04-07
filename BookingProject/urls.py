"""
URL configuration for BookingProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BookingApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),

    path('', views.home_page_view, name='home'),
    path('filter', views.filter_flights_view, name='filter-flights'),
    path('flight/<int:flight_id>', views.show_flight_view, name='show-flight'),
    path('info', views.info_view, name='info'),
    path('register/', views.register_view, name='register'),
    path('register/confirm/<id>/<token>', views.confirm_register_view, name='register-confirm'),
    path('user_info/<user_username>', views.user_info_view, name='user-info'),
    path('ticket/<int:flight_id>', views.book_ticket, name='book-ticket'),
    path('cancel/<int:order_id>', views.cancel_order, name='cancel-order'),
    path('future/orders', views.filter_future_orders, name='future-orders'),
    path('ended_flights', views.filter_ended_orders, name='ended-orders'),
    path('make_review/<int:flight_id>', views.make_review, name='make-review'),
    path('review/<int:review_id>', views.show_review, name='review'),
    path('<int:flight_id>/review', views.show_flight_reviews, name='show-reviews'),
]
