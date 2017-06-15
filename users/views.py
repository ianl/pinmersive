from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import UserProfile
from pins.models import Pin
from relationships.models import UserFollowsUser

from .forms import NewUserForm
from boards.forms import NewBoardForm
from pins.forms import NewPinFromWebForm, NewPinFromDeviceForm

# Create your views here.
def boards(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile
    board_form = NewBoardForm()

    public_boards = user_profile.boards.filter(secret=False)
    secret_boards = user_profile.boards.filter(secret=True)

    return render(request, 'users/boards.html', {
            'user_profile': user_profile, 
            'board_form': board_form, 
            'public_boards': public_boards, 
            'secret_boards': secret_boards
        }
    )

def pins(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile
    pins = Pin.objects.filter(board__user_profile=user_profile, board__secret=False)
    list(set(pins))

    pin_from_web_form = NewPinFromWebForm(user=request.user)
    pin_from_device_form = NewPinFromDeviceForm(user=request.user)

    return render(request, 'users/pins.html', {
            'user_profile': user_profile, 
            'pins': pins, 
            'pin_from_web_form': pin_from_web_form, 
            'pin_from_device_form': pin_from_device_form
        }
    )

# Relationships
def following(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/following.html', {'user_profile': user_profile})

def followers(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/followers.html', {'user_profile': user_profile})

def follow(request, username):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile
            following = get_object_or_404(User, username=username).user_profile

            UserFollowsUser.objects.create(follower=follower, following=following)

    return redirect(reverse('users:user', kwargs={'username': username}))

def unfollow(request, username):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile
            following = get_object_or_404(User, username=username).user_profile

            relationship = get_object_or_404(UserFollowsUser, follower=follower, following=following)
            relationship.delete()

    return redirect(reverse('users:user', kwargs={'username': username}))

# Auths
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)

            login(request, user)
            return redirect('home')
    else:
        form = NewUserForm()
        
    return render(request, 'registration/register.html', {'form': form})
