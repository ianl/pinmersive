from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Pin
from categories.models import Category

from .forms import NewPinForm, EditPinForm

from urllib.parse import urlparse

# Create your views here.
def index(request):
    pins = Pin.objects.filter(board__secret=False)

    return render(request, 'pins/index.html', {'pins': pins})

def show(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.secret and pin.board.user_profile.user != request.user:
        get_object_or_404(Pin, id=None)

    parsed = urlparse(pin.image_url)
    return render(request, 'pins/show.html', {'pin': pin, 'netloc': parsed.netloc})
'''
def create(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user and request.method == 'POST':
        form = NewPinForm(request.POST)

        if form.is_valid():
            form.save()

    return redirect(reverse('users:boards:show', kwargs={
            'username': username, 
            'board_name': form.fields['board']
        })
    )
'''
def edit(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.user_profile.user == request.user and request.method == 'GET':
        form = EditPinForm(instance=pin, user=request.user)
    else:
        return redirect(reverse('pins:show', kwargs={'id': id})) 

    return render(request, 'pins/edit.html', {'pin': pin, 'form': form})

def update(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.user_profile.user == request.user and request.method == 'POST':
        form = EditPinForm(request.POST, instance=pin, user=request.user)

        if form.is_valid():
            form.save()

    return redirect(reverse('pins:show', kwargs={'id': id}))

def destroy(request, id):
    pin = get_object_or_404(Pin, id=id)
    board = pin.board

    if pin.board.user_profile.user == request.user and request.method == 'POST':
        pin.delete()
    else:
        return redirect(reverse('pins:show', kwargs={'id': id}))

    return redirect(reverse('users:boards:show', kwargs={'username': board.user_profile.user.username, 'board_name': board.name})) 