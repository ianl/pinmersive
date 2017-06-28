from django.db import models
from django.contrib.auth.models import User
from relationships.models import UserFollowsUser, UserFollowsBoard

from .helpers import update_filename

# Create your models here.
class UserProfile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to=update_filename, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    follows_users = models.ManyToManyField('self', through='relationships.UserFollowsUser', symmetrical=False, blank=True)
    follows_boards = models.ManyToManyField('boards.Board', through='relationships.UserFollowsBoard', blank=True)

    def __str__(self):
        return self.user.username

    def followers(self):
        relationships = UserFollowsUser.objects.filter(following=self)
        followers = [relationship.follower for relationship in relationships]
        return followers

    def is_following_user_profile(self, user_profile):
        following = UserFollowsUser.objects.filter(follower=self, following=user_profile)
        return True if following.count() > 0 else False

    def is_following_board(self, board):
        following = UserFollowsBoard.objects.filter(follower=self, following=board)
        return True if following.count() > 0 else False