from django.shortcuts import render
from products.models import Product


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def our_story(request):
    """ A view to return the our story page """

    return render(request, 'home/our_story.html')


def taproom(request):
    """ A view to return the our taproom page """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'home/taproom.html', context)


def privacy(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/privacy.html')


def ts_and_cs(request):
    """ A view to return the our privicy page """

    return render(request, 'home/tandcs.html')


