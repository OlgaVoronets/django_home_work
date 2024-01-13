from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from online_store_project import settings
from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Регистрация пройдена',
            message='Тестовое письмо об успешной регистрации',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
            )
        return super().form_valid(form)
