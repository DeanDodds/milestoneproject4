from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db import models
from north_yeast_brewing import settings
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages

from .models import NewletterSubscribers
from .forms import NewletterSubscriberForm



# Create your views here.

def newsletter(request):
    """ Add user newsletter signups to the database """

    if request.method == 'POST':
        # get email address from form
        email = request.POST['newsletter']
        #if user already has already subscripbed 
        if NewletterSubscribers.objects.filter(email = email).exists():
            message = 'Already subscribed'
        # if new email
        else:
            # saves form to database
            NewletterSubscribers.objects.create(email=email)
            # send email confirmation to user
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


def send_newsletter(request):
    """" send a newsletter out to all subscribers """

    if request.method == 'POST':
        # Get data from form 
        subject = request.POST['subject']
        message = request.POST['message']

        # Get emal list from database  
        email_list = []
        for subscriber in NewletterSubscribers.objects.all():
            email_list.append(subscriber.email)

        # send email confirmation to user
        send_mail(
            subject,
            message,
            'northyeastbrewing.com',
            [email_list],
            fail_silently=False,
        )
    
    return render(request, 'newsletter/send_newsletter.html')


def view_email_list(request):
    """ Allow admin to view email list """
    email_list = NewletterSubscribers.objects.all()
    
    context = {
        'email_list': email_list,
    }

    return render(request, 'newsletter/view_email_list.html', context)


def delete_mail(request, email_id):
    """ Allow admin to delete email subscriber from list """
    # find email in database 
    email = get_object_or_404(NewletterSubscribers, pk=email_id)
    # delete email address from databese 
    email.delete()
    # get new mailing list from database 
    email_list = NewletterSubscribers.objects.all()

    context = {
        'email_list': email_list,
    }
    return render(request, 'newsletter/view_email_list.html', context)


def edit_mail(request, email_id):
    """ Allow admin to edit and delete from email list """
    
    if request.method == 'POST':
        updated_email = request.POST['updated-email']
        email = get_object_or_404(NewletterSubscribers, pk=email_id)
        email.email = updated_email
        email.save()

    email_list = NewletterSubscribers.objects.all()
    context = {
        'email_list': email_list,
    }

    return render(request, 'newsletter/view_email_list.html', context)







    
