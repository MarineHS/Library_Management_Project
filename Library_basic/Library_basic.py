from difflib import get_close_matches
import shortuuid

class Book:

    def __init__(self, title, author, ISBN): # Define book object
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = 'available'

    def __str__(self):
        return (f"Title : {self.title} by " 
                f"Author : {self.author}: "
                f"ISBN : {self.ISBN}"
                f" {status}")


class Library:

    def __init__(self): # Define library object
        self.books = []

    def add_book(self, book): # Add a book to the library
        self.books.append(book)
        return f"{book.title} added to the library"

    def book_list(self):
        if not self.books:
            print('No book in library')
        else:
            for books in self.books:
                print(f"{books.title} by {books.author}")

    def find_title(self, title): # Return the list of books thats matches the title
        title_list = list(set([i.title for i in library.books]))
        matches = get_close_matches(title, title_list, n=10, cutoff=0.4)
        if matches:
             print("\n".join(matches))
        else:
            print("This book is not in the library")
        
    def find_author(self, name): # Return the list of possible authors and their books
        author_list = list(set([i.author for i in library.books]))
        matches = get_close_matches(name, author_list, n=5, cutoff=0.5)
        if not matches:
            print('This author was not found in the library')
        for author in matches:
            print(f"{author}:\n" + "\n".join(book.title for book in library.books if book.author == author) + "\n")


class user:

    library = None

    def __init__(self, fname, lname): # Define user and generate a unique ID for each users
        self.ID = self.generate_id()
        self.fname = fname
        self.lname = lname
        self.borrow = []

    @staticmethod
    def generate_id():
        return(shortuuid.ShortUUID().random(length=10))

    @staticmethod
    def error_library():
        if user.library is None:
            raise ValueError('No library has been defined')

    def borrow_book(self, ISBN):#, library): # Borrow a book
        self.error_library()
        book = next((b for b in self.library.books if b.ISBN == ISBN), None)
        if book and (book.status == 'available'):
            self.borrow.append(ISBN)
            book.status = 'borrowed'
            return('You have borrow a book!')
        elif book and book.status == 'borrowed':
            print('This book has already been borrowed.')
        else:
            print("This book isn't in the library.")

    def return_book(self, ISBN):#, library):
        self.error_library()
        if ISBN in self.borrow:
            book = next((b for b in self.library.books if b.ISBN == ISBN), None)
            self.borrow.remove(ISBN)
            book.status = 'available'
            print('You have return your book!')
        else:
            print("You didn't burrow this book.")


# Create empty library
my_library = Library()
#library.book_list()


# Fill library with books
book1 = Book('Harry Potter and the philosopher s stone', 'J. K. Rowling', '147')
my_library.add_book(book1)
book2 = Book('Harry Potter and the chamber of secret', 'J. K. Rowling', '123')
my_library.add_book(book2)
book3 = Book('Wuthering Heights', 'Emily Bronte', '369')
my_library.add_book(book3)
book4 = Book('Jane Eyre', 'Charlotte Bronte', '987')
my_library.add_book(book4)
book5 = Book('My book', 'Hashan', '589')
my_library.add_book(book5)
#library.book_list()

# Test search functions
#library.find_author('River')
#library.find_title('Harry Potter')


# Create user and borrow books
#user.library = my_library
user1 = user('Marine', 'Tanya')
user1.borrow_book('123')
user2 = user('Nicolas', 'Touboul')
user2.borrow_book('123')
