# Basic Library

This script represents the **first design** of this project.

## :hammer:  Functionalities  

This version includes **three main classes**:  
- **Book** → Represents a book with its details  
- **Library** → Manages a collection of books  
- **User** → Represents a library user  

### :books: Book Class  
Each book is created as an **instance** of the `Book` class. A book is defined by:  
- **Title**  
- **Author**  
- **ISBN (unique identifier)**  

By default, all books are marked as **available**.  

Additionally, the `__str__` method has been **overridden** to return a formatted string containing all book details.  

#### :bulb: Example: Creating a book  
```python
book1 = Book('Title', 'Author', 'ISBN')
```

### :office: Library class
The **library** class manages a collection books using a list.

#### :hammer: Main functions
- `add_book(book)` -> Adds a book to the library.
- `book_list()` -> List of all books in library.
- `find_title(title)` -> Returns up to **10 matches** that correspond to the search.
    - If no title matches, it returns a message saying the book is not in the library.
- `find_author` -> Return up to **5 matches** that correspond to the search and the list their books. 
    - If no author matches, it returns a message saying the author was not found.

To find the close match, this class uses **`get_close_matches`** from `difflib`.

#### :bulb: Example 1: Creating a library and add a book 
```python
my_library = Library()
my_library.add_book(book1)
```

#### :bulb: Example2: Search a title  
```python
my_library.find_title('Title')
```

### :bust_in_silhouette: User class

Each **User** instance is defined by a **first name** (`fname`), a **last name** (`lname`) and a **unique ID** generated using a static method.
By default, each user has an **empty list of borrowed books** (`borrow`).

#### :warning: Important
All users share the **same library**, which must be defined before using any functions. Otherwiser, an error message will be raised.

#### :hammer: Main functions
Important: all the user shares the same library and it must be defined before using the functions with `user.library = my_library`. Otherwise, it raises an error message.

- `borrow_book(ISBN)` -> Find the book and check its availability:
    - :heavy_check_mark: **If available**: add to the user's borrowed list and mark it as borrowed.
    - :x: **If already borrowed**: display a message **"This book has already been borrowed"**.
    - :question: **If the ISBN is not found**: returns the message **" This book isn't in the library"**.

- `return_book(ISBN)` -> Find the book in the user's borrowed list:
    - :x: **If the book was not borrowed by the user**: returns the message **"You did not borrow this book"**
    - :heavy_check_mark: **Else**: removes the book from the user's borrowed list and mark it as available

#### :bulb: Example : Create user and borrow a book
```python
user.library = my_library #Assign library
user1 = user('FirstName', 'LastName')
user1.borrow_book('123')
```

## :construction: Improvement
The main issue is that manually creating all the books in the library is **time-consuming**.

### :pushpin: First idea: Import from a CSV file
A possible solution is to create a function that loads books from a CSV file.
We added a method called `library_from_csv` to fill the library with books from a csv file. The csv file contains three columns: title, author and ISBN. The default csv file (`Book_info.csv`) is available in the repository.

#### :bulb: Example : Create a library from a csv file
```python
my_library = Library()
my_library.library_from_csv()
my_library.book_list()
```

### :pushpin: Next step: Using an SQL database
Even with a CSV file, we still need to **rebuild the entire library** each time, which remains inefficient. A better approach would be to use an SQL database to store and manage books dynamically.

This improvement is implemented in the second part of the project, available in the **Library_SQL** folder.