from django.shortcuts import render, get_object_or_404

from .models import Pin
from categories.models import Category

from urllib.parse import urlparse

# Create your views here.
def index(request):
    pins = Pin.objects.all()

    return render(request, 'pins/index.html', {'pins': pins})

def show(request, id):
    pin = get_object_or_404(Pin, id=id)
    parsed = urlparse(pin.image_url)

    return render(request, 'pins/show.html', {'pin': pin, 'netloc': parsed.netloc})