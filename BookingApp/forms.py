from django import forms

from .models import User, Flight


class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150, label='Имя пользователя')
    email = forms.EmailField(max_length=256)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует')
        return email

    def clean(self):
        data = self.cleaned_data
        if data["password1"] != data["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return data


# class BookingForm(forms.Form, forms.ModelForm):
#     amount_of_tickets = forms.IntegerField(min_value=1, max_value=flight.available_seats)
#     class Meta:
#         model = Flight
#     fields = ['airline', 'departure_airport', 'arrival_airport', 'departure_date_time', 'arrival_date_time',
#               'available_seat', 'price']
# # TODO: для max_value как то дать значение flight.available_seats
