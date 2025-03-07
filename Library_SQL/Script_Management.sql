/*
Author: Marine Ha-Shan
This script contains a list of queries useful for managing the Library database
To ensure uniqueness, books are always referenced by their ISBN number, and users by their email address.
*/

-- Find missing data (NULL and empty values) and add missing mail
SELECT * FROM Users
WHERE FirstName IS NULL OR FirstName = ''
   OR LastName IS NULL OR LastName = ''
   OR Mail IS NULL OR Mail = '';

UPDATE Users
SET Mail = 'nathan.carpentier@mail.com'
WHERE FirstName = 'Nathan'
	AND LastName = 'Carpentier'
	AND Mail = ''


-- Find duplicates and remove them
SELECT *
FROM Book
WHERE ISBN IN (
	SELECT ISBN
	FROM Book
	GROUP BY ISBN
	HAVING COUNT(ISBN) > 1)
	
DELETE FROM Book
WHERE BookID = 150


-- Add a book that isn't already in the database
INSERT INTO Book(Title, Author, ISBN)
SELECT 'Hogfather', 'Terry Pratchett', '9780062276285'
WHERE NOT EXISTS (
   SELECT 1
   FROM Book
   WHERE ISBN = '9780062276285'
)


-- Borrow a book
INSERT INTO 
Borrow(BookID, UserID)
VALUES
(
    (SELECT BookID 
		FROM Book 
		WHERE ISBN = '9780062276285'),  
    (SELECT UserID 
		FROM Users 
		WHERE Mail = 'mathieu.dubois@mail.com'),
)

UPDATE Book
SET Available = 0
Where ISBN = '9780062276285'


-- Return a book
DELETE FROM Borrow
WHERE BookID = (
	SELECT BookID 
		FROM Book 
		WHERE ISBN = '9780062276285')

UPDATE Book
SET Available = 1
Where ISBN = '9780062276285'


-- Number of books borrowed
SELECT COUNT(*)
FROM Borrow


-- List of books borrowed by users
SELECT
Book.Title,
Book.Author,
Users.FirstName,
Users.LastName
FROM Book
JOIN Borrow
ON Book.BookID =  Borrow.BookID
JOIN Users
ON Borrow.UserID = Users.UserID


-- List of books borrowed by a specific user
SELECT
Book.Title,
Book.Author
FROM Book
JOIN Borrow
ON Book.BookID =  Borrow.BookID
WHERE Borrow.UserID IN (SELECT UserID FROM Users WHERE Mail = 'louis.moreau@mail.com')


-- List of overdue books
SELECT
Book.Title,
Book.Author,
Users.Mail
FROM Book
JOIN Borrow
ON Book.BookID =  Borrow.BookID
JOIN Users
ON Users.UserID = Borrow.UserID
WHERE Borrow.ReturnDate < GETDATE()