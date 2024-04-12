from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.urls import reverse
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.db.transaction import atomic
from django.utils import timezone
from django.db.models import Q

from .email import ConfirmUserRegisterEmailSender, send_mail
from .forms import RegisterForm, BookingForm, ReviewForm
from .models import Flight, Airline, Airport, User, Order, Review


def home_page_view(request: WSGIRequest):
    """ Домашняя страница """
    flights = Flight.objects.all                 # filter(departure_date_time__gt=timezone.now())
    context: dict = {
        'flights': flights
    }
    return render(request, 'base/home.html', context)


def filter_flights_view(request: WSGIRequest):
    """ Поиск """
    search: str = request.GET.get('search', '')

    if search:
        flight_queryset = Flight.objects.filter(Q(arrival_airport__country__search=search) | Q(departure_airport__country__search=search))
    else:
        return HttpResponseRedirect(reverse('home'))

    context: dict = {
        'flight_queryset': flight_queryset,
        'search_value_form': search,
    }
    return render(request, 'base/home.html', context)


def show_flight_view(request: WSGIRequest, flight_id):
    """ Информация о рейсе """
    try:
        flight: Flight = Flight.objects.get(id=flight_id)

    except Flight.DoesNotExist:
        raise Http404

    if flight.departure_date_time < timezone.now():
        return render(request, 'flight/ended_flight.html', {'flight': flight})

    else:
        return render(request, 'flight/flight.html', {'flight': flight})


def info_view(request: WSGIRequest):
    """ Информация о сайте """
    return render(request, 'base/info.html')


def register_view(request: WSGIRequest):
    """ Страница регистрации """
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                is_active=False,
            )

            ConfirmUserRegisterEmailSender(request, user).send_mail()

            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register-form.html', {'form': form})


def confirm_register_view(request: WSGIRequest, id: str, token: str):
    """ Подтверждение регистрации """
    username = force_str(urlsafe_base64_decode(id))

    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save(update_fields=["is_active"])
        return HttpResponseRedirect(reverse("login"))

    return render(request, "registration/invalid-email-confirm.html", {"username": user.username})


def user_info_view(request: WSGIRequest, user_username):
    """ Информация о пользователе """
    try:
        user: User = User.objects.get(username=user_username)

    except User.DoesNotExist:
        raise Http404

    return render(request, 'user/user_info.html', {'user': user})


@atomic
def book_ticket(request: WSGIRequest, flight_id: int):
    """ Бронирвание билета """
    flight = get_object_or_404(Flight, pk=flight_id)
    form = BookingForm()
    user = request.user

    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'flight': flight})
        if form.is_valid():
            count = form.cleaned_data['count']
            flight.available_seats -= count
            order = Order.objects.create(
                flight=flight,
                user=request.user,
                seats_booked=count,
                total_price=flight.price*count,
            )
            flight.save(update_fields=["available_seats"])

            send_mail(order=order, username=user.username)

            return render(request, 'ticket/ticket.html', {"flight": flight, 'order': order})

    return render(request, 'flight/flight.html', {'booking_form': form, 'flight': flight})


@atomic
def cancel_order(request: WSGIRequest, order_id: int):
    """ Отмена брони """
    order: Order = Order.objects.get(id=order_id)
    order.flight.available_seats += order.seats_booked
    order.flight.save(update_fields=["available_seats"])
    order.delete()
    return HttpResponseRedirect(reverse('home'))


def filter_future_orders(request: WSGIRequest):
    """ Страница с забранированными рейсами """
    orders = Order.objects.filter(flight__departure_date_time__gt=timezone.now())
    context: dict = {'orders': orders}
    return render(request, 'flight/future_flights.html', context)


def filter_ended_orders(request: WSGIRequest):
    """ Страница с забранированными рейсами, которые уже сбылись """
    orders = Order.objects.filter(flight__departure_date_time__lt=timezone.now())
    context: dict = {'orders': orders}
    return render(request, 'flight/ended_flights.html', context)


def make_review(request: WSGIRequest, flight_id: int):
    """ Написание отзыва к сбывшемуся рейсу """
    flight = get_object_or_404(Flight, pk=flight_id)
    form = ReviewForm()
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            review = Review.objects.create(
                flight=flight,
                user=user,
                rating=rating,
                comment=comment,
            )
            review.save()
            return render(request, 'review/review.html', {'review': review})

    return render(request, 'review/make-review.html', {'form': form, 'flight': flight})


def show_review(request: WSGIRequest, review_id: int):
    """ Просмотр отзыва """
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review/review.html', {'review': review})


def show_airline_reviews(request: WSGIRequest, airline_id: int):
    """ Все отзывы о рейсе """
    reviews = Review.objects.filter(flight__airline_id=airline_id)
    return render(request, 'review/reviews-list.html', {'reviews': reviews})


def airline_view(request: WSGIRequest, airline_id: int):
    """ Просмотр авиакомпании """
    airline = get_object_or_404(Airline, pk=airline_id)
    return render(request, 'airline/airline_info.html', {'airline': airline})
