from django.db import models
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

# Create your models here.
class BorrowBook(models.Model):
    isbn = models.ForeignKey('Catalog.Book', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(default= datetime.now() + timedelta(days=21))

    # Override __str__ function
    def __str__(self):
        return f'{self.isbn.title} by {self.user.email}'

    # Remove entry from BorrowBook when book is returned and mark it as available
    def return_book(self):
        self.isbn.available = True # Mark book as available
        self.isbn.save() 
        self.delete() # Delete entry once the book has been returned