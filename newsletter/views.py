from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from .models import NewletterSubscribers


def newsletter(request):
    """ Add user newsletter signups to the database """

    if request.method == 'POST':
        # get email address from form
        email = request.POST['newsletter']
        # if user already has already subscripbed
        if NewletterSubscribers.objects.filter(email=email).exists():
            messages.error(request, 'Already subscribed')
            return redirect('/')
        # if new email
        else:
            # saves form to database
            NewletterSubscribers.objects.create(email=email)
            # send email confirmation to user
            send_mail(
                'North Yeast Brewing',
                'Hey, You have subscriped to the North Yeast Brewing newletter.\
                 We will send you all the lastest events and offers',
                'northyeastbrewing.com',
                [email],
                fail_silently=False,
            )

        context = {
            'email': email,
        }

    return render(request, 'newsletter/newsletter_success.html', context)


@login_required
def send_newsletter(request):
    """" Gets user input then sends a email to newsletter subscriber\
        with vaild email addresss """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be admin to add products.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        # Get data from form
        subject = request.POST['subject']
        message = request.POST['message']

        # Get emal list from database
        email_list = []
        invalid_email = 0
        sent_emails = 0
        
        for subscriber in NewletterSubscribers.objects.all():
            email_list.append(subscriber.email)

        for email in email_list:
            # vaildate email and send to vaid email address
            try:
                validate_email(email)
            except:
                invalid_email = invalid_email + 1
            else:
                sent_emails = sent_emails + 1
                send_mail(
                    subject,
                    message,
                    'northyeastbrewing.com',
                    [email],
                    fail_silently=False,
                )
        messages.success(request, f"Sent newsletter to {sent_emails} email address. { invalid_email} could not sent ")                       

    return render(request, 'newsletter/send_newsletter.html')


@login_required
def view_email_list(request):
    """ Allow admin to view email list """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be admin to edit emails.')
        return redirect(reverse('home'))
    email_list = NewletterSubscribers.objects.all()

    context = {
        'email_list': email_list,
    }

    return render(request, 'newsletter/view_email_list.html', context)


@login_required()
def delete_mail(request, email_id):
    """ Allow admin to delete email subscriber from list """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be admin\
             to delete newsletter emails.')
        return redirect(reverse('home'))
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


@login_required()
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
