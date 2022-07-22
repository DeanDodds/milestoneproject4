from django.urls import path
from django.contrib import messages

from . import views



urlpatterns = [
    path('', views.newsletter, name='newsletter'),
    path('newsletter_success/', views.newsletter, name='newsletter_success'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter'),
    path('view_email_list/', views.view_email_list, name='email_list'),
    path('edit_mail<int:email_id>/', views.edit_mail, name='edit_mail'),
    path('delete_email<int:email_id>/', views.delete_mail, name='delete_mail'),

]
