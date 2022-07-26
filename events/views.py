from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Events
from .forms import EventForm


def events(request):
    """ A view to return the events page """
    events = Events.objects.all()

    context = {
        'events': events,
    }
    return render(request, 'events/events.html', context)


def add_event(request):
    '''Admin can add new events to the database'''
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('events'))
        else:
            messages.error(request, 
                           'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()

    context = {
        'form': form,
    }

    return render(request, 'events/add_events.html', context)


def edit_event(request, event_id):
    """Allows admin to edit events """
    print('edit', event_id)
    event = get_object_or_404(Events, pk=event_id)
    print(event)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Successfully updated event!')
            return redirect(reverse('events'))
        else:
            messages.error(request,
                           'Failed to update Events. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.event_name}')

    context = {
        'form': form,
        'event': event,
    }

    return render(request, 'events/edit_event.html', context)


def delete_event(request, event_id):
    print('delete')
    event = get_object_or_404(Events, pk=event_id)
    event.delete()
    events = Events.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events.html', context)

