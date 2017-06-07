from django.contrib import admin
from .models import UserFollowsUser, UserFollowsBoard

# Register your models here.
admin.site.register(UserFollowsUser)
admin.site.register(UserFollowsBoard)