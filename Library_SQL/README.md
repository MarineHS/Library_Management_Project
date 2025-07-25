# Library featuring SQL database

When we first built our library project, it was clear that initialising the library each time was time-consuming. Therefore, we decided to create a database to store all books and user information. This allows us to update the database using SQL queries (to borrow and return books) or through a Python script.

## Requirements
For the database, I used **SQL Server Management Studio (SSMS) 20**.

## :file_cabinet: The database

The database consists of three tables
- Book
- Users
- Borrow

### :books: Book table

The **Book table** contains the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `BookID` | `INT PRIMARY KEY` | Unique identifier for each book |
| `Title` | `VARCHAR(255)` | Title of the book |
| `Author` | `VARCHAR(255)` | First author of the book |
| `ISBN` | `VARCHAR(13)` | ISBN number |
| `Available` | `BIT DEFAULT 1` | Indicates if the book is available (1) or borrowed (0) |

By default, all books are marked as available.

### :bust_in_silhouette: Users table

The **users table** contains the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `UserID` | `UNIQUEIDENTIFYER PRIMARY KEY DEFAULT NEWID()` | Generates an unique ID for each user |
| `FirstName` | `VARCHAR(255)` | User's first name |
| `LastName` | `VARCHAR(255)` | User's last name |
| `Mail` | `VARCHAR(255)` | User's email address |

### :bookmark: Borrow

The **Borrow table** tracks borrowed books:

| Column Name | Data Type | Description |
| --- | --- | --- |
| `UserID` | `UNIQUEIDENTIFYER` | Generates an unique ID for each user |
| `BookID` | `INT` | User's first name |
| `BorrowDate` | `DATE DEFAULT GETDATE()` | Borrowed date (automatically filled) |
| `ReturnDate` | `DATE DEFAULT DATEADD(DAY, 21, GETDATE())` | Due date (21 days after borrowing) |

### :hammer: Implementation

A script to create the database (if it does not already exist) is available in the repository.

To use it with **SSMS**:

1. Open SQL Server Management Studio.
2. Connect to your database server.
3. Open the `Library_DB.sql` script file.
4. Click Execute to run the script.

Once the database is created, you can get an overview of the tables in SSMS by going to the Tables folder, right-clicking on a table (e.g., dbo.Book), and selecting "Select Top 1000 Rows".

## :clipboard: Library management

Now that the database is created, you can open the second script, which contains various queries useful for managing the library. The queries unable to:

### :broom: Data Cleaning & Integrity
- Find missing data and update it
- Identify duplicated books and remove them

### :bar_chart: Library Management
- Add a book if it is not already in the library
- Record when a user borrows a book and mark the book as unavailable
- Record when a user returns a book and mark the book as available

### :chart_with_upwards_trend: Library Insights
- Count the number of books currently borrowed
- List the books currently borrowed and the users who borrowed them
- List the books borrowed by a specific user
- List overdue books

Feel free to test each query independently and modify it according to your needs.
