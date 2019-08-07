from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth import authenticate

from .forms import RegistrationForm


class RegisterMixin:
    template = None
    form = None

    def post(self, request):
        print(self.form)
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_user = authenticate(username=username,
                                      password=password)
            if login_user:
                login(request, login_user)
            return redirect(reverse('task_list_url'))
        return render(request, self.template,
                      context={'forms': form})


class LoginMixin:
    template = None
    form = None

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_user = authenticate(username=username, password=password)
            if login_user:
                login(request, login_user)
                return redirect(reverse('task_list_url'))
        return render(request, self.template, context={'forms': form})


