from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from BookingApp.models import User


class BaseEmailSender:
    template_name = None
    subject = None
    user_id_field = "pk"

    def __init__(self, request, user: AbstractUser):
        self._request = request
        self._user = user

    def get_template_name(self) -> str:
        if self.template_name is None:
            raise NotImplemented("Вы должны указать имя шаблона в атрибуте класса")
        return self.template_name

    def get_subject(self) -> str:
        if self.subject is None:
            raise NotImplemented("Укажите тему письма в атрибуте класса")
        return self.subject

    def send_mail(self):
        mail = EmailMultiAlternatives(
            subject=self.get_subject() + " на сайте " + self._get_domain(),
            to=[self._user.email]
        )
        mail.attach_alternative(self._get_mail_body(), "text/html")
        mail.send()

    def _get_mail_body(self) -> str:
        context = {
            "user": self._user,
            "domain": self._get_domain(),
            "id": self._get_user_base64(),
            "token": self._get_token(),
        }
        return render_to_string(self.get_template_name(), context)

    def _get_domain(self) -> str:
        return str(get_current_site(self._request))

    def _get_token(self) -> str:
        return default_token_generator.make_token(self._user)

    def _get_user_base64(self) -> str:
        """Кодируем идентификационное поле пользователя, указанное в атрибуте класса"""
        return urlsafe_base64_encode(
            force_bytes(str(getattr(self._user, self.user_id_field)))
        )


class ConfirmUserRegisterEmailSender(BaseEmailSender):
    template_name = "registration/email-confirm.html"
    user_id_field = "username"
    subject = "Подтвердите регистрацию"


def send_mail(order, username: str):
    """
    Отправка билета на почту.
    """

    user: User = User.objects.get(username=username)
    user_email = user.email

    email = EmailMultiAlternatives(
        subject='Ваш билет',
        to=[user_email]
    )

    context: dict = {
        "order": order,
        "user": user,
    }

    content = render_to_string('ticket/ticket-email.html', context)

    email.attach_alternative(content, "text/html")
    email.send()
