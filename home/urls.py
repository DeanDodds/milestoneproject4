from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('our_story', views.story, name='our_story'),
    path('taproom/', views.taproom, name='taproom'),
    path('ts_and_cs/', views.ts_and_cs, name='ts_and_cs'),
    path('privacy/', views.privacy, name='privacy'),
]