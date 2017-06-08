from django.shortcuts import render, get_object_or_404

from .models import Category
from boards.models import Board
from pins.models import Pin

# Create your views here.
def index(request):
    categories = Category.objects.all()

    return render(request, 'categories/index.html', {'categories': categories})

def show(request, name):
    category = get_object_or_404(Category, name=name)
    pins = Pin.objects.filter(board__category=category, board__secret=False)
    list(set(pins))

    return render(request, 'categories/show.html', {'category': category, 'pins': pins})