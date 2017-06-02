from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Board
from users.models import UserProfile

# Create your views here.
def show(request, username, board_name):
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    board = user_profile.board_set.get(name=board_name.lower())
    board_pins = board.pin_set.all()

    return render(request, 'boards/show.html', {'board': board, 'board_pins': board_pins})