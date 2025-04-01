from django.db import models
from PIL import ImageOps

# Create Book model which regroup all attributes 
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    isbn = models.CharField(max_length = 13, unique = True, primary_key=True)
    available = models.BooleanField(default = True)
    summary = models.TextField()
    # Not implemented now but prepare for future update
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    #Override__str__ function
    def __str__(self):
        return f'{self.title} by {self.author}'


    

