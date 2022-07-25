from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def story(request):
    """ A view to return the our story page """

    return render(request, 'home/our_story.html')