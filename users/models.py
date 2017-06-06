from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='user_profile_avatars/', blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    follows_users = models.ManyToManyField('self', through="relationships.UserFollowsUser", symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

    def followers(self):
        relationships = self.follows_users.through.objects.filter(following=self)
        followers = [relationship.follower for relationship in relationships]
        
        return followers