from django.shortcuts import render, redirect
from django.db import models
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

from .models import NewletterSubscribers



# Create your views here.

def newsletter(request):
    """ Add user newsletter signups to the database """
    if request.method == 'POST':
        # get email address from form
        email = request.POST['newsletter']
        #if user already has already subscripbed 
        if NewletterSubscribers.objects.filter(email = email).exists():
            message = 'Already subscribed'
            print(message)
        # if new email
        else:
            # saves form to database
            NewletterSubscribers.objects.create(email=email)
            print('added')
            #send email confirmation to user
            send_mail(
                'North Yeast Brewing',
                'Hey, You have subscriped to the North Yeast Brewing newletter. We will send you all the lastest events and offers',
                'northyeastbrewing.com',
                [email],
                fail_silently=False,
            )


        context = {
            'email': email,
        }

    return render(request, 'newsletter/newsletter_success.html', context)
    
