from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from pins.models import Pin
from relationships.models import UserFollowsUser

from .forms import NewUserForm, EditUserForm, EditUserProfileForm
from boards.forms import NewBoardForm
from pins.forms import NewPinFromWebForm, NewPinFromDeviceForm, NewPinFromPinForm, EditPinForm

# Create your views here.
@login_required
def feed(request):
    feed = Pin.objects.filter(board__secret=False).distinct()
    save_pin_form = NewPinFromPinForm(user=request.user)

    return render(request, 'pins/index.html', {
            'pins': feed,
            'save_pin_form': save_pin_form
        }
    )

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

    if request.user.is_authenticated():
        pin_from_web_form = NewPinFromWebForm(user=request.user)
        pin_from_device_form = NewPinFromDeviceForm(user=request.user)
        save_pin_form = NewPinFromPinForm(user=request.user)
    else:
        pin_from_web_form = NewPinFromWebForm()
        pin_from_device_form = NewPinFromDeviceForm()
        save_pin_form = NewPinFromPinForm()

    return render(request, 'users/pins.html', {
            'user_profile': user_profile, 
            'pins': pins, 
            'pin_from_web_form': pin_from_web_form, 
            'pin_from_device_form': pin_from_device_form,
            'save_pin_form': save_pin_form
        }
    )

@login_required
def settings(request):
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST, instance=request.user)
        edit_user_profile_form = EditUserProfileForm(
            request.POST, 
            request.FILES, 
            instance=request.user.user_profile
        )

        if edit_user_form.is_valid() and edit_user_profile_form.is_valid():
            user = edit_user_form.save()

            user_profile = edit_user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            return redirect(reverse('users:user', kwargs={'username': request.user.username}))

    edit_user_form = EditUserForm(instance=request.user)
    edit_user_profile_form = EditUserProfileForm(instance=request.user.user_profile)

    return render(request, 'users/settings.html', {
            'edit_user_form': edit_user_form,
            'edit_user_profile_form': edit_user_profile_form
        }
    )

# Relationships
def following(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/following.html', {'user_profile': user_profile})

def followers(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/followers.html', {'user_profile': user_profile})

@login_required
def follow(request, username):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile
            following = get_object_or_404(User, username=username).user_profile

            UserFollowsUser.objects.create(follower=follower, following=following)

    return redirect(reverse('users:user', kwargs={'username': username}))

@login_required
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
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == 'POST':
            form = NewUserForm(request.POST)

            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = NewUserForm()

        return render(request, 'registration/register.html', {'form': form})
