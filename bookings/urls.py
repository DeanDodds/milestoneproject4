from django.urls import path
from . import views

urlpatterns = [
    path('manage_bookings/', views.manage_bookings, name='manage_bookings'),
    path('booking_taproom/', views.booking_taproom, name='booking_taproom'),
    path('brewtour/', views.booking_brew_tour, name='book_brew_tour'),
    
]
