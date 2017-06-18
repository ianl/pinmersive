from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Pin
from categories.models import Category

from .forms import NewPinForm, EditPinForm, NewPinFromPinForm

from urllib.parse import urlparse

# Create your views here.
@login_required
def show(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.secret and pin.board.user_profile.user != request.user:
        get_object_or_404(Pin, id=None)

    parsed = urlparse(pin.image_url)
    save_pin_form = NewPinFromPinForm(user=request.user)

    if pin.board.user_profile.user == request.user:
        edit_pin_form = EditPinForm(instance=pin, user=request.user)
    else:
        edit_pin_form = EditPinForm()

    return render(request, 'pins/show.html', {
            'pin': pin, 
            'netloc': parsed.netloc, 
            'save_pin_form': save_pin_form,
            'edit_pin_form': edit_pin_form
        }
    )

@login_required
def create(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user and request.method == 'POST':
        form = NewPinForm(request.POST, request.FILES)

        if form.is_valid():
            pin = form.save()
            return redirect(reverse('pins:show', kwargs={'id': pin.id}))

    return redirect(reverse('users:boards:show', kwargs={
            'username': username, 
            'board_name': pin.board.name
        })
    )

@login_required
def edit(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.user_profile.user == request.user and request.method == 'GET':
        form = EditPinForm(instance=pin, user=request.user)
    else:
        return redirect(reverse('pins:show', kwargs={'id': id})) 

    return render(request, 'pins/edit.html', {'pin': pin, 'form': form})

@login_required
def update(request, id):
    pin = get_object_or_404(Pin, id=id)

    if pin.board.user_profile.user == request.user and request.method == 'POST':
        form = EditPinForm(request.POST, instance=pin, user=request.user)

        if form.is_valid():
            form.save()

    return redirect(reverse('pins:show', kwargs={'id': id}))

@login_required
def destroy(request, id):
    pin = get_object_or_404(Pin, id=id)
    board = pin.board

    if pin.board.user_profile.user == request.user and request.method == 'POST':
        pin.delete()
    else:
        return redirect(reverse('pins:show', kwargs={'id': id}))

    return redirect(reverse('users:boards:show', kwargs={'username': board.user_profile.user.username, 'board_name': board.name})) 

@login_required
def save(request, id):
    pin = get_object_or_404(Pin, id=id)

    if request.method == 'POST':
        form = NewPinForm(request.POST)

        if form.is_valid():
            pin_copy = form.save(commit=False)
            pin_copy.image_url = pin.image_url
            pin_copy.save()

            return redirect(reverse('pins:show', kwargs={'id': pin_copy.id}))

    return redirect(reverse('pins:show', kwargs={'id': pin.id}))

def search(request):
    query = request.GET['q']

    query_list = query.split()
    list(set(query_list))
    pins = Pin.objects.filter(board__secret=False).distinct()

    result = []
    for q in query_list:
        for pin in pins.filter(Q(description__icontains=q) | Q(board__name__icontains=q) | Q(board__description__icontains=q) | Q(board__category__name__icontains=q)):
            if pin not in result:
                result.append(pin)

    return render(request, 'pins/index.html', {'pins': result})
