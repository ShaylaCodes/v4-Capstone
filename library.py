#Welcome to our library! 
#You will see some comments floating around explaining some of the concepts. 
#You can find more information on the README.md file!

from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import Error
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import date

load_dotenv()
# The lines above are importing different modules in Python that are used throughout the project.
DB_HOST =os.getenv('DB_HOST')
DB_NAME =os.getenv('DB_NAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_USER =os.getenv('DB_USER')
DB_PORT =os.getenv('DB_PORT')
# This is connecting the database to the python script
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
            )
        print( DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
        self.cur = self.conn.cursor()

    def execute(self, query, PARAM=None, which_query='r'):
        try:
            print("Executing query:", query)
            self.cur.execute(query, PARAM)
            if which_query == 'w':
                self.conn.commit()
            print('The query was successful!')
        except (Exception, psycopg2.DatabaseError) as error:
            print('Oops.. something went wrong.',query)
            print(error)
        finally:
            if which_query == 'r':
                if self.cur.description is not None: 
                    return self.cur.fetchall()
                else:
                    return []
            
    def __del__(self):
        self.conn.close()
# The Database class is connecting the railway database and setting up the ability to add in queries efficiently in the upcoming functions.

class Book:
    def __init__(self, title, author, category, status):
        self.category = category
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Status: {self.status}'
# This is creating the class named 'Book' and creating 4 arguments. To add on, it has a string function for readability.

class Member:
    def __init__(self, member_id,first_name,last_name, join_date, database):
        self.database = database
        self.name = f'{first_name} {last_name}'
        self.member_id = member_id
        self.borrowed_books = []
        self.join_date = join_date

    def get_borrowed_books(self):
        query= f"SELECT * FROM borrowed_books WHERE member_id={self.member_id}"
        borrowed_books = self.database.execute(query)
        for book in borrowed_books:
            self.borrowed_books.append(book.book_id)
            return borrowed_books

    def borrow_book(self, book):
        borrow_date = date.today()
        if book.status == 'Available':
            book.status = 'Checked Out'
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed {book.title}.')
            #sql query to change the status of the book
            query = f"""
            UPDATE books
            SELECT status FROM books WHERE book.id = {book.id}
            SET status = 'Checked Out'
            """
            #sql query to add a record to borrow books table
            query = f"""
            INSERT INTO borrowed_books (member_id, book_id, borrow_date)
            VALUES ({self.member_id}, {book.id}, {borrow_date})
            """
        else:
            print(f'This book is currently borrowed by someone else.')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.status = 'Available'
            self.borrowed_books.remove(book)
            print(f'{self.name} returned {book.title}.')

        else:
            print(f'{self.name} did not borrow {book.title}.')
# This is returning a book, if it has been borrowed, in order for it to be available again. 

    def __str__(self):
        borrowed_titles = ', '.join(
            [book.title for book in self.borrowed_books])
        return f'Member Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {borrowed_titles}'
# This function is ensuring it is readable for the human eye.

    def number_of_borrowed_books(self,query): 
        database.execute(query="""
        SELECT DATE_FORMAT(borrow_date,'%%Y-%%m') AS date,COUNT(*) AS num_borrowed_books
        FROM borrowed_books
        GROUP BY DATE_FORMAT(borrow_date,'%Y-%m')
        """)
    
    def num_active_members(self,query): 
        query="""
        SELECT DATE_FORMAT(borrow_date,'%%Y-%%m') AS month, COUNT(*) AS active_members
        FROM borrowed_books
        WHERE borrow_date <= return_date AND (return_date IS NULL OR return_date>= DATE_FORMAT(borrow_date, '%%Y-%%m-01'))
        GROUP BY month 
        """
        #Selcts the number of books from each category by using 
    def num_books_per_category(self,query):
        query="""
        SELECT c.name_category, COUNT(*) AS num_books
        FROM books
        JOIN category c ON books.category = c.category
        JOIN borrowed_books bb ON books = bb.books
        GROUP BY c.name_category: 
        """
        #Selects the top 3 most borrowed books from borrowed_books table by using the book_id and matching it with member_id
    def top_3_borrowed_books(self,query): 
        query ="""
        SELECT b.book_id , b.book_title, COUNT(*) AS borrowed_books 
        FROM books
        JOIN borrowed_books bb ON b.books_id = bb.books_id 
        GROUP BY b.book_id, b.book_title
        GROUP BY borrow_count DESC 
        LIMIT 3;
        """
        #Selects the top 3 active members from borrowed_books table by using the member_id 
    def top_3_active_members(self,query): 
        query = """
        SELECT m.member_id, m.first_name, m.last_name, COUNT(*) AS borrowed_books 
        FROM library_members m 
        JOIN borrowed_books bb ON m.member_id = bb.member_id 
        WHERE bb.return_date IS NOT NULL 
        GROUP BY m.member_id, m.first_name, m.last_name
        LIMIT 3;
        """ 
        #Selects the most active member from borrowed_books table by using the member_id
    def most_active_member(self,query): 
        query ="""
        SELECT m.member_id, m.first_name, m.last_name, COUNT(*) AS borrowed_books 
        FROM library_members m 
        JOIN borrowed_books bb ON m.member_id = bb.member_id 
        GROUP BY m.member_id, m.first_name, m.last_name
        GROUP BY borrowed_books DESC
        LIMIT 1;
        """
# The book class is connecting the functions to the database and carrying out a multitide of actions. 
class Library:
        #Data Visualization
    def num_books_borrowed_top3_active(self): 
       # COUNT(member_id) to count number of books borrowed from table.
        query = f"""
        SELECT COUNT(b.member_id) AS num_borrowed_books, m.first_name, m.last_name
        FROM borrowed_books b
        INNER JOIN library_members m ON b.member_id = m.member_id
        GROUP BY b.member_id,m.first_name, m.last_name
        ORDER BY num_borrowed_books DESC
        LIMIT 3;
        """
        results = self.database.execute(query)
        print(results)
       
        member_ids =[]
        num_books_borrowed =[]
       
        for row in results:
            borrowed_books = row[0]
            first_name = row[1]
            last_name = row[2]
            
        
            member_ids.append(f"{first_name} {last_name}")
            num_books_borrowed.append(borrowed_books)
        
        plt.bar(member_ids, num_books_borrowed)
        plt.xlabel("Top 3 Members")
        plt.ylabel("Books Borrowed")
        plt.title("Top 3 Members with the Most Books Borrowed")
        plt.show()
        plt.savefig('bar-graph.svg',format='svg')
        

    def __init__(self,database):
        self.database = database 
        self.catalog = self.get_books()
        self.members = self.get_members()

    def get_books(self):
        books_data = self.database.execute("SELECT * FROM books")
        books = []
        for book in books_data:
            books.append(Book(book[0], book[1], book[2], book[3]))  # Append each book to the books list
        return books  # Return the list of books


    def get_members(self):
        members_data = self.database.execute("SELECT * FROM library_members")
        members = []
        for member in members_data:
            members.append(Member(member[0], member[1], member[2], member[3], self.database))
        return members
    # Demonstrates all members in the 'library_members' table

    def add_book(self, title, author, category):
        book = Book(title, author, category, 'Available')
        self.catalog.append(book)
        print(f'{book.title} was added to the catalog.')
        #query to add a book into the book table by inserting the author, title and category of the book
        self.database.execute(f"""
        INSERT INTO Books (author, title, status, category)
        VALUES ('{author}', '{title}', 'available', '{category}');
        """, which_query='w')
    # This adds in a book into the table called 'Books' & also adds in the author, category, and if its available or not. 

    def remove_book(self, title):
        #query used to remove a book by inputting the title of the book
        self.database.execute("DELETE FROM books WHERE title = %s",(title,),which_query='w')
        return "Book has been removed successfully."
    
    def register_member(self,member_id,name,join_date):
        join_date = date.today()
        member = Member(self,name, member_id,join_date, database)
        self.members.append(member)
        print(f'{member.name} was registered.')
        [first_name, last_name] = name.split(" ")
        #query to register a new member into library_members by inputting "member_id" and "name"
        self.database.execute(f"""
            INSERT INTO library_members (member_id, first_name, last_name, join_date)
            VALUES ('{member_id}', '{first_name}', '{last_name}', '{join_date}');
        """, which_query='w')
        
    
    def borrow_book(self, member_id,book_id):
        borrow_date = date.today()
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is not None:
            book = None
            for b_id in self.catalog:
                if b_id.book_id == book_id:
                    book = b_id
                    break
            if book is not None:
                member.borrow_book(book)
            else:
                print(f'Book not found.')
        else:
            print(f'Member not found.')
        #query used to borrow a book from borrowed_books table by using your "member_id" and "book_id"
        self.database.execute("""
        INSERT INTO borrowed_books(member_id,book_id,borrow_date)
        VALUES (%s,%s,%s);
        """,(member_id,book_id,borrow_date), which_query='w')
       
    def return_book(self, member_id, book_id):
        return_date = date.today()
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is not None:
            book = None
            for b in self.catalog:
                if b.book_id == book_id:
                    book = b
                    break
            if book is not None:
                member.return_book(book)
            else:
                print(f'Book not found.')
        else:
            print(f'Member not found.')
        #query updates the date at which you checked a book out and returns the book to the date of return.
        query=(f"""
         UPDATE borrowed_books
         SET return_date = '{return_date}'
         WHERE member_id= '{member_id}' AND book_id = '{book_id}'
        """)
        self.database.execute(query, which_query='w')
        
        
                
    
    def display_all_books(self):
        print('\n'.join(str(book) for book in self.catalog))

    def display_all_members(self):
        print('\n'.join(str(member) for member in self.members))      
# The library class is connecting the database to functions and carrying them out. The functions connect to the the data directly. 
# This means that when you utilize those functions, it also changed the table in railway. 

database = Database()
library = Library(database)
#library.add_book("Hatchet","Mccoy","Adventure")- adds a book into books
#library.register_member("member_id","name")- adds member_id and name to library_members
#library.remove_book("book_title")- removes the book from book table by entering the title of the book
#library.borrow_book("member_id","book_id")- borrows the book by using your "member_id" and "book_id"
#library.return_book("member_id","book_id")- returns the book you borrowed from borrowed_books table by inputting your "member_id" and "book_id" and returns the 'return_date' to todays date
#library.display_all_books()- displays all available books for checkout 
#library.display_all_members()- displays all members in library_members 
library.num_books_borrowed_top3_active()



