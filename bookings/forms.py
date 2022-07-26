from .models import BreweryTourBooking, TaproomBooking
from django.forms import ModelForm
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BreweryTourBookingForm(forms.ModelForm):
    class Meta:
        model = BreweryTourBooking
        exclude = ['date_booked', ]
        widgets = {
            'date': DateInput(),
        }


class TaproomBookingBookingForm(forms.ModelForm):
    class Meta:
        model = TaproomBooking
        exclude = ['date_booked', ]
        widgets = {
            'date': DateInput(),
        }
