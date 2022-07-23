from .models import Message
from django import forms


class ContactForm(forms.ModelForm):

    class Meta:
        model = Message
        exclude = ['received']
    