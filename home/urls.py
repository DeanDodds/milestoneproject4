from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our_story', views.story, name='our_story'),
    path('taproom', views.taproom, name='taproom'),
]