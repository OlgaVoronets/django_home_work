import random

from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from online_store_project import settings
from users.forms import UserRegisterForm, NewPasswordForm
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


def get_new_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        # new_password = BaseAbstractUser().manager.make_random_password()
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            subject='Пароль изменен',
            message=f'Ваш новый пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    else:
        form = NewPasswordForm
        context = {
            'form': form
        }
        return render(request, 'users/new_password.html', context)

