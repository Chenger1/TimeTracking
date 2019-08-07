from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.views.generic import View

from .utils import RegisterMixin
from .utils import LoginMixin

from .forms import RegistrationForm
from .forms import LoginForm
# Create your views here.


class RegisterView(RegisterMixin, View):
    template = 'users/register.html'
    form = RegistrationForm

    def get(self, request):
        return render(request, self.template,
                      context={'forms': self.form})


class LoginView(LoginMixin,View):
    template = 'users/login.html'
    form = LoginForm

    def get(self, request):
        return render(request, self.template,
                      context={'forms': self.form})


class LogOutView(View):

    @staticmethod
    def logout(request):
        logout(request)
        return redirect(reverse('main_url'))