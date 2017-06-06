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
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    user_boards = user_profile.board_set.all()

    return render(request, 'users/boards.html', {"user_profile": user_profile, "user_boards": user_boards})

def board(request, username, board_name):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    board = user_profile.board_set.get(name=board_name.lower())

    return render(request, 'users/board.html', {'board': board, 'user_profile': user_profile})

# Pins
def pins(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    user_pins = []
    for board in user_profile.board_set.all():
        for pin in board.pin_set.all():
            user_pins.append(pin)
    list(set(user_pins))

    return render(request, 'users/pins.html', {"user_profile": user_profile, "user_pins": user_pins})

# Relationships
def following(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    return render(request, 'users/following.html', {"user_profile": user_profile})

def followers(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    return render(request, 'users/followers.html', {"user_profile": user_profile})

def follow(request, username):
    if request.method == 'POST':
        if username != request.user.username:
            user = User.objects.get(username=username)
            following = UserProfile.objects.get(user=user)
            follower = request.user.user_profile

            UserFollowsUser.objects.create(follower=follower, following=following)

    return redirect(reverse('users:user', kwargs={'username': username}))

def unfollow(request, username):
    if request.method == 'POST':
        if username != request.user.username:
            user = User.objects.get(username=username)
            following = UserProfile.objects.get(user=user)
            follower = request.user.user_profile

            relationship = get_object_or_404(UserFollowsUser, follower=follower, following=following)
            relationship.delete()

    return redirect(reverse('users:user', kwargs={'username': username}))