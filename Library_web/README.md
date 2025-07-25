# Web Interface with Django

## Project Overview

The site is divided into three main sections:
- **the home page**. Display the library's oppening hours and a list of available activities
- **the catalog page**. Features a search bar  to find books by title or author; and a highlight section showcasing the books of the month.
- **the login page**. Allows both users and admin to log into their account using their email address.

Navigation between pages is done via the top navigation bar.

## App Structure

The site is built around four Django apps.

**The main app**

This app contains the templates for the home page.

**The catalog app**

The catalog app is used to manage the library’s book collection and includes the search functionality.

Each book is identified by its ISBN. Additional information such as the title, author, summary and book cover can be added. Once a book is created, it is automatically marked as available for borrowing. It can also be flagged as featured to appear in the highlight section.

When a user search for a book (or an author), the app returns a list of matching results. The user can then click on a specific book to view its detailed information.

**The management app**

This app handles the borrowing and returning of books. It updates book availability automatically and tracks due dates. If a book is returned late, a warning is generated for the administrator.

**The user app**

The user app manages both basic and admin users which are identified by their mail address.

*Basic users*

Basic users can view the books they have borrowed and their due dates in their account. If a book is overdue, it is highlighted in red.

*Admin users*

Admin users can manage (add, remove, update) the books and users databases. They receive alerts if a book is overdue.

## Getting Started


**Requirements**

The website was developped with under Python version 3.8.1. All the following commands are meant to be executed from a terminal. Before launching the site, make sure to create and activate a virtual environment and install the required packages:

```python
# Activate environnement
.\env\Scripts\activate

# Doanwload required packages
pip install -r requirements.txt
```

**Load database**

The file *DataLibrary.json* provides a sample catalog of books and users that can be used as test.

```python
# Migrate the models
python manage.py makemigrations
python manage.py migrate

# Load database
python manage.py loaddata DataLibrary.json
```

**Navigating the website**

To run the website loacally:

```python
python manage.py runserver
```

This will give you an url (ex: http://127.0.0.1:8000/) that you can open in your browser. You'll be able to navigate the site and even log in as different users (I think Louis Moreau needs to check his account. He has an overdue book!).

To log in as a user, user their email in the format firstname.lastname@mail.com (ex: louis.moreau@mail.com). The password follows the format DjangoFirstnameDatebirth (ex: DjangoLouis1999).

:warning: To access the admin interface, you can:
- give permissions to an existing user. Here is how to give stall permissions to Nicolas Carpentier. 

```python
# Enter Django shell
python .\manage.py shell

#Inside the shell
# Import libraries
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

# Select admin
user = CustomUser.objects.get(email="nicolas.carpentier@mail.com")

# Give admin permissions
perms = ['Catalog.view_book', 'users.change_customuser', 'Catalog.add_book', 'users.view_customuser', 'management.view_borrowbook', 'Catalog.change_book', 'users.add_customuser', 'management.add_borrowbook', 'management.change_borrowbook']

for codename in perms:
    permission = Permission.objects.get(codename=codename)
    user.user_permissions.add(permission)
```

- create a superuser and follow the prompts to create a full admin account with all permissions

```python
python .\manage.py createsuperuser
```
