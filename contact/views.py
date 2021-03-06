from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Message

from .forms import ContactForm


def contact(request):
    """ A view to return the Contact page """

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for you \
            enquiry we will get back to you as soon as we can')
        else:
            messages.error(request, 'sorry \
            something went wrong there please try again')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)


@login_required()
def view_messages(request):
    """ A view to return the Messages page """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be \
                       admin to view user messages.')
        return redirect(reverse('home'))

    user_messages = Message.objects.all()

    context = {
        'user_messages': user_messages,
    }

    return render(request, 'contact/view_messages.html', context)


@login_required()
def delete_message(request, message_id):
    ''' delete user messages '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you must be admin \
                       to delete user messages.')
        return redirect(reverse('home'))

    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    messages.success(request, 'message deleted')

    user_messages = Message.objects.all()

    context = {
        'user_messages': user_messages,
    }
    return render(request, 'contact/view_messages.html', context)
