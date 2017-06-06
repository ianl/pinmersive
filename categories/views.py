from django.shortcuts import render

from .models import Category
from boards.models import Board
from pins.models import Pin

# Create your views here.
def index(request):
    categories = Category.objects.all()

    return render(request, 'categories/index.html', {'categories': categories})

def show(request, name):
    pins = Pin.objects.filter(board__category__name=name)
    list(set(pins))

    return render(request, 'categories/show.html', {'category_name': name, 'pins': pins})