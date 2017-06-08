from django.db import models
from relationships.models import UserFollowsBoard

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    secret = models.BooleanField(default=False)

    user_profile = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='boards')
    category = models.ForeignKey('categories.Category', blank=True, null=True, related_name='boards')

    class Meta:
        unique_together = ('user_profile', 'name')

    def clean(self):
        self.name = self.name.lower()

    def __str__(self):
        return str(self.user_profile.user.username) + "'s " + str(self.name)

    def followers(self):
        relationships = UserFollowsBoard.objects.filter(following=self)
        followers = [relationship.follower for relationship in relationships]
        
        return followers