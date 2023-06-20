from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import Error

load_dotenv()

DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('PASS')
DB_PORT = os.getenv('PORT')

class Database:
   def __init__(self):
    self.conn = psycopg2.connect(
       host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
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
    def close(self):
         self.connection.close()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = 'available'

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Status: {self.status}'


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def get_borrowed_books(self,database):
        query= f"SELECT * FROM borrowed_books WHERE member_id={self.member_id}"
        
    
    
    def borrow_book(self, book):
        if book.status == 'available':
            book.status = 'borrowed'
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed {book.title}.')
        else:
            print(f'This book is currently borrowed by someone else.')

    def number_of_borrowed_books(self,query): 
        query="""SELECT DATE_FORMAT(borrow_date. '%Y-%m') AS date,COUNT(*) AS num_borrowed_books
        FROM borrowed_books
        GROUP by month 
        GROUP by month"""
        self.cursor.execute(query) 
        result = self.cursor.fetchall()
        return results 
    
    def num_active_members(self,query): 
        query="""
        SELECT DATE_FORMAT(borrow_date,'%%Y-%%m') AS month, COUNT(*) AS active_members
        FROM borrowed_books
        WHERE borrow_date <= return_date(borrow_date) AND (return_date IS NULL OR return_date>= DATE_FORMAT(borrow_date, '%%Y-%%m-01'))
        GROUP BY month 
        GROUP BY month 
        """
        self.cursor.execute(query) 
        results = self.cursor.fetchall() 
        return results 
    
    def num_books_per_category(self,query):
        query="""
        FROM books
        JOIN category c ON books.category = c.category
        JOIN borrowed_books bb ON books = bb.books
        GROUP BY c.name_category: 
        """
        self.cursor.exectue(query) 
        results = self.cursor.fetchall()
        return results 

    def top_3_borrowed_books(self,query): 
        query ="""
        SELECT b.book_id , b.book_title, COUNT(*) AS borrowed_books 
        FROM books
        JOIN borrowed_books bb ON b.books_id = bb.books_id 
        GROUP BY b.book_id, b.book_title
        GROUP BY borrow_count DESC 
        LIMIT 3;
        """
        self.cursor.execute(query) 
        results = self.cursor.fetchall()
        return results 
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
        self.cursor.exectte(query) 
        results = self.cursor.fetchall()
        return results 
    def most_active_member(self,query): 
        query ="""
        SELECT m.member_id, m.first_name, m.last_name, COUNT(*) AS borrowed_books 
        FROM library_members m 
        JOIN borrowed_books bb ON m.member_id = bb.member_id 
        GROUP BY m.member_id, m.first_name, m.last_name
        GROUP BY borrowed_books DESC
        LIMIT 1;
        """
        self.cursor.execute(query) 
        results = self.cursor.fetchall()
        return results 
    


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


class Library:
    def __init__(self):
        self.catalog = query = """
        SELECT Books FROM library;
        """
        self.cursor.execute(query)
        self.conn.commit()
        print(self.cur.fetchall())


        self.members = query = """
        SELECT members * from library
        """
        self.cursor.execute(query)
        self.conn.commit()
        print(self.cur.fetchall())


    def add_book(self, title, author, query):
        book = Book(title, author)
        self.catalog.append(book)
        print(f'{book.title} was added to the catalog.')

        query = """
        INSERT INTO Book (author, title, status)
        VALUES (add_book);
        """
        self.cursor.execute(query)
        self.conn.commit()

    def remove_book(self, title, query):
        for book in self.catalog:
            if book.title == title:
                self.catalog.remove(book)
                print(f'{book.title} was removed from the catalog.')
                return
        print(f'Book not found.')
        query = """
        "DELETE FROM Books WHERE title = input('book being removed')";
        """
        self.cursor.execute(query)
        self.conn.commit()
    
    def register_member(self, name, member_id, query):
        member = Member(name, member_id)
        self.members.append(member)
        print(f'{member.name} was registered.')
        query = """
        "INSERT INTO member (name, member_id)
        VALUES (adding_member));
        """
        self.cursor.execute(query)
        self.conn.commit()

    def borrow_book(self, member_id, title, query):
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

        self.query = """
        "member"
        """
        self.cursor.execute(query)
        self.conn.commit()

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

    def display_all_books(self):
        print('\n'.join(str(book) for book in self.catalog))

    def display_all_members(self):
        print('\n'.join(str(member) for member in self.members))

database = Database()
library = Library()
library.add_book('lfsefejslkjf', 'slfhlesf')