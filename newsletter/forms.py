from django import forms
from .models import NewletterSubscribers

class NewletterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewletterSubscribers
        fields = ['email', ]
