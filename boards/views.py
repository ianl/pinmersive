from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from .models import Board
from relationships.models import UserFollowsBoard

from .forms import NewBoardForm, EditBoardForm

# Create your views here.
def show(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    return render(request, 'boards/show.html', {'board': board})

def create(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user and request.method == 'POST':
        form = NewBoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.user_profile = request.user.user_profile
            board.save()

    return redirect(reverse('users:boards', kwargs={'username': username})) 

def edit(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    if user_profile.user == request.user and request.method == 'GET':
        form = EditBoardForm(instance=board)
    else:
        return redirect(reverse('users:boards:show', kwargs={'username': username, 'board_name': board.name})) 

    return render(request, 'boards/edit.html', {'board': board, 'form': form})

def update(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    if user_profile.user == request.user and request.method == 'POST':
        form = EditBoardForm(request.POST, instance=board)

        if form.is_valid():
            form.save()

    return redirect(reverse('users:boards:show', kwargs={'username': username, 'board_name': board.name}))

def destroy(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    if user_profile.user == request.user and request.method == 'POST':
        board.delete()
    else:
        return redirect(reverse('users:boards:show', kwargs={'username': username, 'board_name': board.name}))

    return redirect(reverse('users:boards', kwargs={'username': username}))  

# Relationships
def followers(request, username, board_name):
    user_profile = get_object_or_404(User, username=username).user_profile
    board = get_object_or_404(user_profile.boards, name=board_name.lower())

    return render(request, 'boards/followers.html', {'board': board})

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