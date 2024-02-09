from django.urls import path
from .views import Register,Homepage

app_name='authentication'

urlpatterns = [
    path('register/', Register, name='register'),
    path('homepage/', Homepage, name='homepage'),
]