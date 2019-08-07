from django.urls import path
from django.urls import include

from .views import MainView

urlpatterns = [
    path('', MainView.get, name='main_url'),
    path('user/', include('users.urls')),
    path('task/', include('tasks.urls')),
]