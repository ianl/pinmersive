from django.shortcuts import render
from django.contrib.auth.models import User

from users.models import UserProfile
from boards.models import Board
from pins.models import Pin

# Create your views here.

#Boards
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

#Pins
def pins(request, username):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    user_pins = []
    for board in user_profile.board_set.all():
        for pin in board.pin_set.all():
            user_pins.append(pin)
    list(set(user_pins))

    return render(request, 'users/pins.html', {"user_profile": user_profile, "user_pins": user_pins})