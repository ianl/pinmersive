from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Board
from pins.models import Pin
from relationships.models import UserFollowsBoard

from .forms import NewBoardForm, EditBoardForm
from pins.forms import NewPinFromWebForm, NewPinFromDeviceForm, NewPinFromPinForm

# Create your views here.
def show(request, username, board_name):
    user = get_object_or_404(User, username=username)
    board = get_object_or_404(user.user_profile.boards, name=board_name.lower())

    if board.secret and user != request.user:
        get_object_or_404(Board, name=None)

    if request.user.is_authenticated() and request.user == user:
        pin = Pin(board=board)
        pin_from_web_form = NewPinFromWebForm(instance=pin, user=user)
        pin_from_device_form = NewPinFromDeviceForm(instance=pin, user=user)
        board_edit_form = EditBoardForm(instance=board)
    else:
        pin_from_web_form = NewPinFromWebForm()
        pin_from_device_form = NewPinFromDeviceForm()
        board_edit_form = EditBoardForm()

    return render(request, 'boards/show.html', {
            'board': board, 
            'board_edit_form': board_edit_form,
            'pin_from_web_form': pin_from_web_form, 
            'pin_from_device_form': pin_from_device_form
        }
    )

@login_required
def create(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user and request.method == 'POST':
        form = NewBoardForm(request.POST)

        if form.is_valid():
            board = form.save(commit=False)
            board.user_profile = request.user.user_profile
            board.save()
            
            return redirect(reverse('users:boards:show', kwargs={
                        'username': username, 
                        'board_name': board.name
                    }
                )
            ) 

    return redirect(reverse('users:boards', kwargs={'username': username}))

@login_required
def update(request, username, board_name):
    user = get_object_or_404(User, username=username)
    board = get_object_or_404(user.user_profile.boards, name=board_name.lower())

    if user == request.user and request.method == 'POST':
        form = EditBoardForm(request.POST, instance=board)

        if form.is_valid():
            form.save()

    return redirect(reverse('users:boards:show', kwargs={
                'username': username, 
                'board_name': board.name
            }
        )
    )

@login_required
def destroy(request, username, board_name):
    user = get_object_or_404(User, username=username)
    board = get_object_or_404(user.user_profile.boards, name=board_name.lower())

    if user == request.user and request.method == 'POST':
        board.delete()
    else:
        return redirect(reverse('users:boards:show', kwargs={
                    'username': username, 
                    'board_name': board.name
                }
            )
        )

    return redirect(reverse('users:boards', kwargs={'username': username}))  

# Relationships
def followers(request, username, board_name):
    user = get_object_or_404(User, username=username)
    board = get_object_or_404(user.user_profile.boards, name=board_name.lower())

    if board.secret and user != request.user:
        get_object_or_404(Board, name=None)

    return render(request, 'boards/followers.html', {'board': board})

@login_required
def follow(request, username, board_name):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile

            board_user = get_object_or_404(User, username=username)
            following = get_object_or_404(board_user.user_profile.boards, name=board_name.lower())

            if following.secret:
                get_object_or_404(Board, name=None)

            UserFollowsBoard.objects.create(follower=follower, following=following)

    return redirect(reverse('users:boards:show', kwargs={
                'username': username, 
                'board_name': board_name
            }
        )
    )

@login_required
def unfollow(request, username, board_name):
    if request.method == 'POST':
        if username != request.user.username:
            follower = request.user.user_profile

            board_user = get_object_or_404(User, username=username)
            following = get_object_or_404(board_user.user_profile.boards, name=board_name.lower())

            if following.secret:
                get_object_or_404(Board, name=None)

            relationship = get_object_or_404(UserFollowsBoard, follower=follower, following=following)
            relationship.delete()

    return redirect(reverse('users:boards:show', kwargs={
                'username': username, 
                'board_name': board_name
            }
        )
    )
