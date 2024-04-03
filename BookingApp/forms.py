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


class BookingForm(forms.Form):
    count = forms.IntegerField(min_value=1, max_value=1220, required=True)

    def clean_count(self):
        flight: Flight = self.initial['flight']
        count: int = self.cleaned_data['count']
        if count > flight.available_seats:
            raise forms.ValidationError("Количество билетов превышает допустимое")
        return count


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=254)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError("Пользователя с таким email не существует")
