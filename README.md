# Bookstore.py

# Bookstore Clerk Program - README

This program is designed for bookstore clerks to manage a database of books. The program provides various functionalities, such as adding new books, updating book information, deleting books, and searching the database for specific books.

## Table of Contents

1. [Database Setup](#database-setup)
2. [Functionality](#functionality)
   - [Adding New Books](#adding-new-books)
   - [Updating Book Information](#updating-book-information)
   - [Deleting Books](#deleting-books)
   - [Searching Books](#searching-books)
   - [Exiting the Program](#exiting-the-program)

## Database Setup <a name="database-setup"></a>

To use this program, follow these steps to set up the database:

1. Create a database called "ebookstore".
2. Inside the "ebookstore" database, create a table called "books".
3. The "books" table should have the following structure:

   - id (integer)
   - Title (text)
   - Author (text)
   - Qty (integer)

4. Populate the "books" table with the provided values. You can also add your own values if desired.

## Functionality <a name="functionality"></a>

The program provides the following functionalities for the bookstore clerk:

### Adding New Books <a name="adding-new-books"></a>

- The clerk can choose the option "Enter book" from the menu.
- The program prompts the clerk to enter the details of a new book, including the title, author, and quantity.
- The entered book is added to the database table.

### Updating Book Information <a name="updating-book-information"></a>

- The clerk can choose the option "Update book" from the menu.
- The program prompts the clerk to enter the ID of the book to update.
- The program then allows the clerk to update the book's title, author, or quantity.
- The updated information is saved in the database table.

### Deleting Books <a name="deleting-books"></a>

- The clerk can choose the option "Delete book" from the menu.
- The program prompts the clerk to enter the ID of the book to delete.
- The book with the specified ID is removed from the database table.

### Searching Books <a name="searching-books"></a>

- The clerk can choose the option "Search books" from the menu.
- The program prompts the clerk to enter a search keyword (title or author) to find a specific book.
- The program searches the database table and displays the matching books, if found.

### Exiting the Program <a name="exiting-the-program"></a>

- The clerk can choose the option "Exit" from the menu to exit the program.

Feel free to customize and enhance the program based on your specific needs and preferences.
