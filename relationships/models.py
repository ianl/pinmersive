from django.db import models

# Create your models here.
class UserFollowsUser(models.Model):
    follower = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE, related_name='following')

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return str(self.follower.user.username) + " follows " + str(self.following.user.username)

class UserFollowsBoard(models.Model):
    follower = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    following = models.ForeignKey("boards.Board", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return str(self.follower.user.username) + " follows " + str(self.following.user_profile.user.username) + "'s " + str(self.following.name)