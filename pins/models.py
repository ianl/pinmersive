from django.db import models
from django.core.validators import URLValidator
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import uuid
from urllib.request import urlopen
from urllib.parse import urlsplit
import os

def update_filename(instance, filename):
    path = 'pin_images/'

    ext = filename.split('.')[-1]
    format = str(instance.id) + '.' + str(ext)

    return os.path.join(path, format)

# Create your models here.
class Pin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(max_length=2000, validators=[URLValidator()], blank=True)
    image_file = models.ImageField(upload_to=update_filename, blank=True)

    board = models.ForeignKey('boards.Board', on_delete=models.CASCADE, related_name='pins')

    def save(self, *args, **kwargs):
        if not self.image_url and not self.image_file:
            return

        super(Pin, self).save(*args, **kwargs)

        if self.image_url and not self.image_file:
            self.save_image_from_url()
        elif self.image_file and not self.image_url:
            self.image_url = self.image_file.url
            self.save()

    def __str__(self):
        return str(self.id)

    def save_image_from_url(self):
        image = NamedTemporaryFile(delete=True)
        image.write(urlopen(self.image_url).read())
        image.flush()

        ext = urlsplit(self.image_url).path.split('.')[-1]
        fname = str(self.id) + '.' + str(ext)

        self.image_file.save(fname, File(image))
        self.save()