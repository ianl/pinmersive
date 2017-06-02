from django.db import models

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    secret = models.BooleanField(default=False)

    user_profile = models.ForeignKey("users.UserProfile", on_delete=models.CASCADE)
    category = models.ForeignKey("categories.Category", blank=True, null=True)

    class Meta:
        unique_together = ("user_profile", "name")

    def clean(self):
        self.name = self.name.lower()

    def __str__(self):
        return self.name