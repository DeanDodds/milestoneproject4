from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('messages/', views.view_messages, name='messages'),
    path('delete_message/<int:message_id>/',
         views.delete_message, name='delete_message'),
]
