from django.db import models
from PIL import Image, ImageOps

# Create Book model
class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    isbn = models.CharField(max_length = 13, unique = True, primary_key=True)
    available = models.BooleanField(default = True)
    summary = models.TextField()
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    book_of_the_month = models.BooleanField(default=False)

    #Override __str__ function
    def __str__(self):
        return f'{self.title} by {self.author} ({self.isbn})'


    

