from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_check = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']

        if User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'This user already register'},
                                  code='user exists')
        if password != password_check:
            raise ValidationError({'password': '', 'password_check': 'Password does not exists.'},
                                  code='Passwords do not exist')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = User.objects.get(username=username)
        if not User.objects.filter(username=username).exists():
            raise ValidationError({'username': 'This username does not register'},
                                  code='user exits')
        if user and not user.check_password(password):
            raise ValidationError({'password': 'Password in wrong'},
                                  code='password incorrect')