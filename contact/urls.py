from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('messages/', views.messages, name='messages'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('reply_to_message/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('send_email_message<int:message_id>/', views.send_email_message, name='send_email_message'),
]