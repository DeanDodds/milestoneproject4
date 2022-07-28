from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BreweryTourBooking, TaproomBooking
from .forms import BreweryTourBookingForm, TaproomBookingBookingForm


def booking_brew_tour(request):
    """ Returns the brewtour success template and saves user data"""
    if request.method == 'POST':
        form = BreweryTourBookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            name = request.POST['name']
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
    """ Returns Taproom booking sucess page and save the users data """

    if request.method == 'POST':
        form = TaproomBookingBookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            name = request.POST['name']
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
        form = TaproomBookingBookingForm()

        context = {
            'form': form,
        }
        return render(request, 'bookings/taproom_booking.html', context)


@login_required
def manage_bookings(request):
    """Returns the manage booking template allowing admin to see bookings"""
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, you must be admin to view bookings.')
        return redirect(reverse('home'))
    taproom_bookings = TaproomBooking.objects.all()
    brewtours_booking = BreweryTourBooking.objects.all()

    context = {
       'taproom': taproom_bookings,
       'brewtour': brewtours_booking,
    }

    return render(request, 'bookings/bookings.html', context)
