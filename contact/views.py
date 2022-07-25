from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Message

from .forms import ContactForm

# Create your views here.

def contact(request):
    """ A view to return the Contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()


    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)


def messages(request):
    """ A view to return the Messages page """

    user_messages = Message.objects.all()

    context = {
        'user_messages': user_messages,
    }

    return render(request, 'contact/view_messages.html', context)


def delete_message(request, message_id):
    ''' delete user messages '''
    print(message_id)
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    user_messages = Message.objects.all()

    context = {
        'user_messages': user_messages,
    }
    return render(request, 'contact/view_messages.html', context)


def reply_to_message(request, message_id):
    """ Allows admin to reply to user messages """
    message = get_object_or_404(Message, pk=message_id)

    context = {
        'message': message,
    }
    return render(request, 'contact/reply.html', context)


def send_email_message(request, message_id):
    """ Allows admin to reply to messages """
    if request.method == 'POST':
        # Get data from form
        email = request.POST.get['to_email']
        subject = request.POST.get['subject']
        reply_message = request.POST.get['message']
        print(email, subject, reply_message)

        # send email to user
        send_mail(
            subject,
            message,
            'northyeastbrewing.com',
            [email],
            fail_silently=False,
        )
        message = get_object_or_404(Message, pk=message_id)

        context = {
            'message': message,
        }
        return render(request, 'contact/view_messages.html', context)