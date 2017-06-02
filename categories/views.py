from django.shortcuts import render

from .models import Category
from boards.models import Board

# Create your views here.
def index(request):
    categories = Category.objects.all()

    return render(request, 'categories/index.html', {'categories': categories})

def show(request, name):
    category = Category.objects.get(name=name)
    boards = Board.objects.filter(category=category)

    pins = []
    for board in boards:
        for pin in board.pin_set.all():
            pins.append(pin)
    list(set(pins))

    return render(request, 'categories/show.html', {'category_name': name, 'pins': pins})