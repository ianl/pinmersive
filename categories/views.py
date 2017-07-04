from django.shortcuts import render, get_object_or_404

from .models import Category
from boards.models import Board
from pins.models import Pin

from pins.forms import NewPinFromPinForm

# Create your views here.
def show(request, name):
    category = get_object_or_404(Category, name=name)
    pins = Pin.objects.select_related().filter(board__category=category, board__secret=False).prefetch_related('board__category')

    return render(request, 'categories/show.html', {
            'category': category, 
            'pins': pins
        }
    )
