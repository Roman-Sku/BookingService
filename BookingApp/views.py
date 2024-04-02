from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Q, Case, When
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views import View

from .email import ConfirmUserRegisterEmailSender
from .forms import RegisterForm
from .models import Flight, Airline, Airport, User, Order, Review


def home_page_view(request: WSGIRequest):
    flights = Flight.objects.all()
    context: dict = {
        'flights': flights
    }
    return render(request, 'home.html', context)


# TODO: def

def filter_flights_view(request: WSGIRequest):
    search: str = request.GET.get('search', '')

    if search:
        flight_queryset = Flight.objects.filter(arrival_date_time__icontains=search)
    else:
        flight_queryset = Flight.objects.all()

    context: dict = {
        'flight_queryset': flight_queryset,
        'search_value_form': search,
    }
    return render(request, 'home.html', context)  # TODO: пофиксить поиск при пустом значении строки search


def show_flight_view(request: WSGIRequest, flight_id):
    try:
        flight: Flight = Flight.objects.get(id=flight_id)

    except Flight.DoesNotExist:
        raise Http404

    return render(request, 'flight.html', {'flight': flight})


def info_view(request: WSGIRequest):
    return render(request, 'info.html')


def register_view(request: WSGIRequest):
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
    username = force_str(urlsafe_base64_decode(id))

    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save(update_fields=["is_active"])
        return HttpResponseRedirect(reverse("login"))

    return render(request, "registration/invalid-email-confirm.html", {"username": user.username})


def user_info_view(request: WSGIRequest, user_username):
    try:
        user: User = User.objects.get(username=user_username)

    except User.DoesNotExist:
        raise Http404

    return render(request, 'user_info.html', {'user': user})


def book_ticket_view(request: WSGIRequest, flight_id: str):
    try:
        flight: Flight = Flight.objects.get(flight_id=flight_id)
    except Flight.DoesNotExist:
        raise Http404
    return render(request, 'book_ticket.html', {'flight': flight})


def book_ticket(request: WSGIRequest, flight_id: int):
    if request.method == "POST":
        flight: Flight = Flight.objects.get(id=flight_id)
        flight.available_seats = request.POST.get("available_seats")
        flight.available_seats -= 1
        flight.save(update_fields=["available_seats"])
        flight: Flight = Flight.objects.get(id=flight_id)

        return render(request, 'ticket.html', {'flight': flight})
