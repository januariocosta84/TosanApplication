from django.contrib import admin
from django.urls import path
from .views import sign_up, login_view, receiver_dashboard

urlpatterns = [
    path('register/', sign_up, name='signup'),
    path('login/', login_view, name='login'),
    path('receiver-dash/', receiver_dashboard, name='receiver'),
]
