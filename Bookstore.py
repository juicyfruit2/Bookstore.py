import sqlite3
db = sqlite3.connect('ebookstore')
cursor = db.cursor()


#created a table data

cursor.execute('''CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Qty INTEGER)''')
db.commit()

#list of books to inside into table

id_1 = 3001
Title_1 = 'A Tale of Two Cities'
Author_1 = 'Charles Dickens'
Qty_1 = 30

id_2 = 3002
Title_2 = "Harry Potter and the Philosopher's Stone"
Author_2 = 'J.K. Rowling'
Qty_2 = 40

id_3 = 3003
Title_3 = "The Lion, the Witch and the Wardrobe"
Author_3 = 'C.S. Lewis'
Qty_3 = 25

id_4 = 3004
Title_4 = 'The Lord of the Rings'
Author_4 = 'J.R.R Tolkien'
Qty_4 = 37

id_5 = 3005
Title_5 = 'Alice in Wonderland'
Author_5 = 'Lewis Carroll'
Qty_5 = 12


#added data into table using execute many

books = [(id_1,Title_1,Author_1,Qty_1),(id_2,Title_2,Author_2,Qty_2),(id_3,Title_3,Author_3,Qty_3),(id_4,Title_4,Author_4,Qty_4),(id_5,Title_5,Author_5,Qty_5)]

#added exception error to allow database to keep working

try:
 cursor.executemany('''INSERT INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)''',(books))
except Exception as e:
 db.commit()

#  created a User Menu

user_input = ""

while user_input != "Exit":

 user_input = input('''please enter one of the following functions:
                    
1.View Books
2.Enter book
3.Update book
4.Delete book
5.Search books
6.Exit: \n ''')

 if user_input == "6":
  db.close()
  break

#View all books in database, displaying information in user friendly way
 elif user_input == "1":
   cursor.execute('''SELECT id,Title,Author,Qty FROM books WHERE id> 0''')
   book = cursor.fetchall()
   print("\nBOOKS IN DATABASE(id,Title,Author,Quantity)\n")
   for i in book:
    print(f"{i}\n")

# enter new book function, with confirmation message of inputs and defensive programming to prevent invalid datatypes being entered
 elif user_input == "2":

#defensive programming used to ensure user only enters integer data type
   new_id = ""
   while new_id != int:
    try:
     new_id = int(input("Please enter id of new book: "))
     break
    except ValueError:
     print("Please only enter an integer number")

   new_title = input("Please enter title of new book: ")
   print("Title confirmed")

   new_author = input("Please enter author of new book: ")
   print("Author confirmed")

#defensive programming used to ensure user only enters integer data type
   new_qty = ""
   while new_qty != int:
    try:
     new_qty = int(input("Please enter quantity of new book: "))
     break
    except ValueError:
     print("Please only enter an integer number")
   print("Quantity confirmed")

   cursor.execute('''INSERT INTO books(id,Title,Author,Qty) VALUES(?,?,?,?)''',
                   (new_id, new_title, new_author, new_qty))
   print(f"id:{new_id} Title:{new_title} has been added to the database ")

#update book function, confirming user input and display user information in friendly manner
 elif user_input == "3":

   choice = input("What would you like to update: id/Title/Author/Quantity: ")
   choice = choice.lower()

   if choice == 'id':

    # defensive programming used to ensure user only enters integer data type
    id = ""
    while id != int:
     try:
      id = int(input("Please enter id book: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    # defensive programming used to ensure user only enters integer data type
    new_id = ""
    while new_id != int:
     try:
      new_id = int(input("Please enter the new id of book: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    print("Input confirmed")
    cursor.execute('''UPDATE books SET id = ? WHERE id = ? ''', (new_id, id))
    print(f"id for book has been updated")

   elif choice == 'title':

    # defensive programming used to ensure user only enters integer data type
    id = ""
    while id != int:
     try:
      id = int(input("enter id of book you want to update: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    new_title = input("Enter the new title of the book:")
    print("Input confirmed")
    cursor.execute('''UPDATE books SET Title = ? WHERE id = ? ''', (new_title, id))
    print(f"Title for book {id} has been updated")

   elif choice == 'author':

    # defensive programming used to ensure user only enters integer data type
    new_id = ""
    while new_id != int:
     try:
      new_id = int(input("Please enter id of the book: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    new_author = input("Enter new author of the book: ")
    print("Input confirmed")
    cursor.execute('''UPDATE books SET Author = ? WHERE id = ? ''', (new_author, id))
    print(f"Author for book {id} has been updated")

   elif choice == 'quantity':

    # defensive programming used to ensure user only enters integer data type
    id = ""
    while id != int:
     try:
      id = int(input("Please enter id of the book: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    # defensive programming used to ensure user only enters integer data type

    new_qty = ""
    while new_qty != int:
     try:
      new_qty = int(input("Enter new quantity of the book: "))
      break
     except ValueError:
      print("Please only enter an integer number")

    print("Input confirmed")
    cursor.execute('''UPDATE books SET Qty = ? WHERE id = ? ''', (new_qty, id))
    print(f"Quantity for book {id} has been updated")


#delete book function asking user to confirm deletion
 elif user_input == "4":

# defensive programming used to ensure user only enters integer data type

  id = ""
  while id != int:
   try:
    id = int(input("Please enter id of the book: "))
    break
   except ValueError:
    print("Please only enter an integer number")

  cursor.execute('''SELECT Title FROM books WHERE id =?''', (id,))
  book = cursor.fetchone()
  choice = input( f"Are you sure you want to delete book:{book} with id:{id}. Enter 'Y' to delete or 'N' to return to menu: ")
  choice = choice.lower()

  if choice == "y":
   cursor.execute('''DELETE FROM books WHERE id = ? ''', (id,))
   print("Book has been deleted")

  elif choice == "n":
   print("Book not deleted")


 #search specific book in database function and display information in user friendly manner
 elif user_input == "5":

   id = ""
   while id != int:
    try:
     id = int(input("Enter id of the book: "))
     break
    except ValueError:
     print("Please only enter an integer")

   cursor.execute('''SELECT id FROM books WHERE id =? ''', (id,))
   book_id = cursor.fetchone()
   print(f"id:{book_id}")

   cursor.execute('''SELECT Title FROM books WHERE id =? ''', (id,))
   book_title = cursor.fetchone()
   print(f"Title:{book_title}")

   cursor.execute('''SELECT Author FROM books WHERE id =? ''', (id,))
   book_author = cursor.fetchone()
   print(f"Author:{book_author}")

   cursor.execute('''SELECT Qty FROM books WHERE id =? ''', (id,))
   book_qty = cursor.fetchone()
   print(f"Quantity:{book_qty}")

 else:
  print("Invalid input please try again !")
