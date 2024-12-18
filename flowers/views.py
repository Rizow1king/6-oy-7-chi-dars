from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *


def index(request: WSGIRequest):
    flowers = Flowers.objects.filter(published=True)
    context = {
        'flowers': flowers
    }

    return render(request, 'index.html', context)


def category(request: WSGIRequest, type_id):
    type = get_object_or_404(Categories, id=type_id)
    flowers = Flowers.objects.filter(type_id=type_id, published=True)
    context = {
        'types': [type],
        'flowers': flowers
    }

    return render(request, 'index.html', context)


def flower(request: WSGIRequest, flower_id):
    flower = get_object_or_404(Flowers, id=flower_id, published=True)

    context = {
        'flower': flower
    }
    return render(request, 'detail.html', context)
