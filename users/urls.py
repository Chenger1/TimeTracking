from django.urls import path

from .views import RegisterView
from .views import LoginView
from .views import LogOutView

urlpatterns = [
    path('registration/', RegisterView.as_view(),
         name='registration_url'),
    path('login/', LoginView.as_view(),
         name='login_url'),
    path('logout/', LogOutView.logout,
         name='logout_url')
]