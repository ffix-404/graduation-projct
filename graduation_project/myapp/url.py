from django.urls import path
from . import views

urlpatterns = [
    path('signin_login', views.signin_login, name='signin_login'),
    path('home', views.home, name='home')
    # ... your other URLs ...
]