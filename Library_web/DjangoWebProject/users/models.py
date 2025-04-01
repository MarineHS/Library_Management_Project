from django.db import models
from catalog.models import Book
from shortuuidfield import ShortUUIDField
from django.utils.timezone import now


# Contain informations for each users
class LibraryUser(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    # If the mail is already registred in the data base, raise an error message
    mail = models.EmailField(unique=True)
    # Create a unique random ID for each users
    userID = ShortUUIDField(primary_key=True)

    # Override __str__ function
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class BorrowBook(models.Model):
    book = models.OneToOneField(Book, to_field='isbn', on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(LibraryUser, to_field='userID', on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} \t {self.LibraryUser.mail}'

    # Set return_date and update Book.available
    def set_return_date(self):
        if not self.return_date:
            self.return_date = self.borrow_date + timedelta(days=21)
            self.book.available = False

        self.book.save()
        self.save()

    # Mark a book as available and delete the entry from the BorrowBook Table
    def return_book(self, isbn):
        if self.book.isbn == isbn:
            self.book.available = True
            self.book.save()
            BorrowBook.objects.filter(book__isbn==isbn).delete()

    # Get the list of books not returned after duedate and the person who borrowed it
    def late_books_list(self):
        late_borrows = BorrowBook.objects.filter(return_date__lt=now())
        if late_borrows.exists():
            print("Late Books: ")
        for borrow in late_borrows:
            print(f'{borrow.user.firstname} {borrow.user.lastname} did not return "{borrow.book.title}" on time! (Due: {borrow.return_date.date()})')
        else:
            return(None)
