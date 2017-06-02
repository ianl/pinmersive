from django.shortcuts import render

from .models import Pin

from urllib.parse import urlparse

# Create your views here.
def index(request):
    pins = Pin.objects.all()

    return render(request, 'pins/index.html', {'pins': pins})

def show(request, id):
    pin = Pin.objects.get(id=id)
    parsed = urlparse(pin.image_url)

    return render(request, 'pins/show.html', {'pin': pin, 'netloc': parsed.netloc})