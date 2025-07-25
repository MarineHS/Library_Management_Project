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

Database available (books and some users with password*) need to be uploaded
\* how we got the passwords
Need to give access to admin
run with manage.py