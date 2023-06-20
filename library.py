from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import Error
import matplotlib.pyplot as plt 
import numpy as np 
import datetime

load_dotenv()
DB_HOST =os.getenv('DB_HOST')
DB_NAME =os.getenv('DB_DATABASE')
DB_USER =os.getenv('DB_USER')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_PORT =os.getenv('DB_PORT')

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
        host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
            )
        self.cur = self.conn.cursor()

    def execute(self,query,PARAM=None,which_query='r'):
        try:
            self.cursor.execute(query,PARAM)
        except:
            print('Oops..something went wrong.',query)
        finally:
            if which_query=='r':
                print(self.cur.fetchall())
            if which_query=='w':
               self.conn.commit()
               print('The query was successful!') 
            else:
                print('Oops..something went wrong.')
    def __del__(self):
        self.conn.close()

class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Status: {self.status}'

class Member:
    def __init__(self, name, member_id, database):
        self.database = database
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def get_borrowed_books(self,book):
        query= f"SELECT * FROM borrowed_books WHERE member_id={self.member_id}"
        if book.status =='borrowed':
            print(self.title,'has been borrowed by',self.name)
        else:
            print("Books is available", self.title,'by',self.author)

    def borrow_book(self, book):
        if book.status == 'available':
            book.status = 'borrowed'
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed {book.title}.')
            query = f"""
            UPDATE books
            SELECT status FROM books WHERE book.id = {book.id}
            SET status = 'borrowed'
            """
            #sql query to change the status of the book
            #sql query to add a record to borrow books table
        else:
            print(f'This book is currently borrowed by someone else.')
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.status = 'available'
            self.borrowed_books.remove(book)
            print(f'{self.name} returned {book.title}.')
        else:
            print(f'{self.name} did not borrow {book.title}.')

    def __str__(self):
        borrowed_titles = ', '.join(
            [book.title for book in self.borrowed_books])
        return f'Member Name: {self.name}, Member ID: {self.member_id}, Borrowed Books: {borrowed_titles}'
    
    def number_of_borrowed_books(self,query): 
        query="""
        SELECT DATE_FORMAT(borrow_date,'%%Y-%%m') AS date,COUNT(*) AS num_borrowed_books
        FROM borrowed_books
        GROUP BY DATE_FORMAT(borrow_date,'%Y-%m')
        """
    
    def num_active_members(self,query): 
        query="""
        SELECT DATE_FORMAT(borrow_date,'%%Y-%%m') AS month, COUNT(*) AS active_members
        FROM borrowed_books
        WHERE borrow_date <= return_date AND (return_date IS NULL OR return_date>= DATE_FORMAT(borrow_date, '%%Y-%%m-01'))
        GROUP BY month 
        """
    
    def num_books_per_category(self,query):
        query="""
        FROM books
        JOIN category c ON books.category = c.category
        JOIN borrowed_books bb ON books = bb.books
        GROUP BY c.name_category: 
        """

    def top_3_borrowed_books(self,query): 
        query ="""
        SELECT b.book_id , b.book_title, COUNT(*) AS borrowed_books 
        FROM books
        JOIN borrowed_books bb ON b.books_id = bb.books_id 
        GROUP BY b.book_id, b.book_title
        GROUP BY borrow_count DESC 
        LIMIT 3;
        """
    
    def top_3_active_members(self,query): 
        query = """
        SELECT m.member_id, m.first_name, m.last_name, COUNT(*) AS borrowed_books 
        FROM library_members m 
        JOIN borrowed_books bb ON m.member_id = bb.member_id 
        WHERE bb.return_date IS NOT NULL 
        GROUP BY m.member_id, m.first_name, m.last_name
        GROUP BY borrowed_books DESC 
        LIMIT 3;
        """ 
    
    def most_active_member(self,query): 
        query ="""
        SELECT m.member_id, m.first_name, m.last_name, COUNT(*) AS borrowed_books 
        FROM library_members m 
        JOIN borrowed_books bb ON m.member_id = bb.member_id 
        GROUP BY m.member_id, m.first_name, m.last_name
        GROUP BY borrowed_books DESC
        LIMIT 1;
        """

class Library:
    
    def __init__(self,database):
        self.database = database 
        self.catalog = database.execute("""
        SELECT * FROM books;
        """)
        
        self.members = database.execute("""
        SELECT first_name, last_name FROM library_members;
        """)

    def get_books(self, database):
        books_data = database.execute("SELECT * FROM books")
        print(books_data)
        books = [Book(book_id, title, author, category, status)
        for book_id, title, author, category, status in books_data]
        return books

    def add_book(self, title, author, category):
        book = Book(title, author)
        self.catalog.append(book)
        print(f'{book.title} was added to the catalog.')
        database.execute(f"""
        INSERT INTO Books (author, title, status, category)
        VALUES ({author}, {title}, "available", {category});
        """)

    def remove_book(self, title):
        for book in self.catalog:
            if book.title == title:
                self.catalog.remove(book)
                print(f'{book.title} was removed from the catalog.')
                return
        print(f'Book not found.')
        database.execute("""
        "DELETE FROM Books WHERE title = input('book being removed')";
        """)
    
    def register_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f'{member.name} was registered.')
        [first_name, last_name] = name.split(" ")
        database.execute(f"""
        "INSERT INTO library_members (first_name, last_name, join_date)
        VALUES ({first_name}, {last_name}, {datetime.now()});
        """)

    def borrow_book(self, member_id, title):
        
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is not None:
            book = None
            for b in self.catalog:
                if b.title == title:
                    book = b
                    break
            if book is not None:
                member.borrow_book(book)
            else:
                print(f'Book not found.')
        else:
            print(f'Member not found.')

        database.execute ( """
        "INSERT INTO borrowed_books"
        """)

    def return_book(self, member_id, title):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if member is not None:
            book = None
            for b in self.catalog:
                if b.title == title:
                    book = b
                    break
            if book is not None:
                member.return_book(book)
            else:
                print(f'Book not found.')
        else:
            print(f'Member not found.')
        database.execute ("""
        "member"
        """)

    def display_all_books(self):
        print('\n'.join(str(book) for book in self.catalog))

    def display_all_members(self):
        print('\n'.join(str(member) for member in self.members))      

database = Database()
library = Library(database)
library.add_book('lfsefejslkjf', 'slfhlesf')