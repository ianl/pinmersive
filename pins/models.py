from django.db import models
from django.core.validators import URLValidator
import uuid

# Create your models here.
class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255)
    image_url = models.URLField(max_length=2000, validators=[URLValidator()])
    image_file = models.ImageField(upload_to='pin_images/')

    board = models.ForeignKey("boards.Board", on_delete=models.CASCADE)