from django.db.models.signals import pre_save
from django.dispatch import receiver
from PIL import Image
import os

# Reshape each book cover and save in the database
@receiver(pre_save, sender=Book)
def resize_cover(sender, instance, **kwargs):
    if instance.cover:
        img_path = instance.cover.path
        with Image.open(img_path) as img:
            img = img.resize((300, 450))
            img.save(img_path)