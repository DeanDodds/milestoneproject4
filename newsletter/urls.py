from django.urls import path
from django.contrib import messages

from . import views



urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('newsletter_signup/', views.newsletter, name='newsletter_signup')
]
