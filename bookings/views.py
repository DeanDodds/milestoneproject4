from django.shortcuts import render, get_object_or_404, redirect,reverse
import datetime
from .models import BreweryTourBooking, TaproomBooking
from .forms import BreweryTourBookingForm, TaproomBookingBookingForm



# Create your views here.


def booking_brew_tour(request):

   if request.method == 'POST':
      form = BreweryTourBookingForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()

         name = request.POST['name']
         email = request.POST['email']
         date = request.POST['date']
         time = request.POST['time']
         people = request.POST['number_of_people']


         context = {
            'name': name,
            'date': date,
            'time': time,
            'people': people,
         }
         
         return render(request, 'bookings/brewtour_success.html', context)
   else:
      form = BreweryTourBookingForm() 

   context = {
      'form': form,
   }

   return render(request, 'bookings/brew_tour_booking.html', context)



def booking_taproom(request):
   print('taproom')
   if request.method == 'POST':
      form = TaproomBookingBookingForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()

         name = request.POST['name']
         email = request.POST['email']
         date = request.POST['date']
         time = request.POST['time']
         people = request.POST['number_of_people']


         context = {
            'name': name,
            'date': date,
            'time': time,
            'people': people,
         }
         
         return render(request, 'bookings/taproom_success.html', context)
   else:
      print('where here')
      form = TaproomBookingBookingForm()


      context = {
      'form': form,
      }
      return render(request, 'bookings/taproom_booking.html', context)


def manage_bookings(request):

   taproom_bookings = TaproomBooking.objects.all()
   brewtours_booking = BreweryTourBooking.objects.all()
   
   context= {
      'taproom': taproom_bookings,
      'brewtour': brewtours_booking,
   }
   return render(request, 'bookings/bookings.html', context)