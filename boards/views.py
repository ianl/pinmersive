from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Board
from relationships.models import UserFollowsBoard

# Create your views here.
def show(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    return render(request, 'boards/show.html', {'user_profile': user_profile, 'board': board})

def follow(request, username, board_name):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile

            user_profile_of_board = get_object_or_404(User, username=username).user_profile
            following = get_object_or_404(user_profile_of_board.boards, name=board_name.lower())

            UserFollowsBoard.objects.create(follower=follower, following=following)

    return redirect(reverse('users:boards:show', kwargs={'username': username, 'board_name': board_name}))

def unfollow(request, username, board_name):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile

            user_profile_of_board = get_object_or_404(User, username=username).user_profile
            following = get_object_or_404(user_profile_of_board.boards, name=board_name.lower())

            relationship = get_object_or_404(UserFollowsBoard, follower=follower, following=following)
            relationship.delete()

    return redirect(reverse('users:boards:show', kwargs={'username': username, 'board_name': board_name}))