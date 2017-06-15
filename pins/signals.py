from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Pin

@receiver(post_delete, sender=Pin)
def destroy_image_file(sender, instance, **kwargs):
    if instance.image_file:
        instance.image_file.delete(save=False)