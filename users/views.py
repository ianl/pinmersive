from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from users.models import UserProfile
from boards.models import Board
from pins.models import Pin
from relationships.models import UserFollowsUser

# Create your views here.

# Boards
def boards(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/boards.html', {"user_profile": user_profile})

def board(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    return render(request, 'users/board.html', {'user_profile': user_profile, 'board': board})

# Pins
def pins(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile
    pins = Pin.objects.filter(board__user_profile=user_profile)
    list(set(pins))

    return render(request, 'users/pins.html', {"user_profile": user_profile, "pins": pins})

# Relationships
def following(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/following.html', {"user_profile": user_profile})

def followers(request, username):
    user_profile = get_object_or_404(User, username=username).user_profile

    return render(request, 'users/followers.html', {"user_profile": user_profile})

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