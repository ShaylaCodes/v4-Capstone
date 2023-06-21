from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import Error
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import date

load_dotenv()

DB_HOST =os.getenv('DB_HOST')
DB_NAME =os.getenv('DB_NAME')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_USER =os.getenv('DB_USER')
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
            print('Oops.. something went wrong.', query)
            print(error)
        finally:
            if which_query == 'r':
                if self.cur.description is not None: 
                    return self.cur.fetchall()
                else:
                    return []
            else:
                 print('Oops.. something went wrong.')
        
    
    def __del__(self):
        self.conn.close()

class Book:
    def __init__(self, title, author, category, status):
        self.category = category
        self.title = title
        self.author = author
        self.status = status
    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, Status: {self.status}'

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
            VALUES ({self.member_id}, {book.id}, {datetime.datetime.now()})
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
    
    def num_books_borrowed_top3_active(self): 
       # COUNT(member_id) to count number of books borrowed from table.
        member_ids = [self.members[6],self.members[7],self.members[12]]
        num_books_borrowed=[]
        for member_id in member_ids:
            query = f"""
            SELECT COUNT(member_id) AS num_borrowed_books
            FROM borrowed_books 
            WHERE member_id = {member_id}
        """
        results = self.database.execute(query)
        if results:
              num_books_borrowed.append(results[0][0])
        else:
              num_books_borrowed.append(0)
        plt.bar(member_ids,num_books_borrowed) 
        plt.xlabel("Top 3 Members")
        plt.ylabel("Books Borrowed")
        plt.title("Top 3 active members")
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

    def add_book(self, title, author, category):
        book = Book(title, author, category, 'Available')
        self.catalog.append(book)
        print(f'{book.title} was added to the catalog.')
        self.database.execute(f"""
        INSERT INTO Books (author, title, status, category)
        VALUES ('{author}', '{title}', 'available', '{category}');
        """, which_query='w')

    def remove_book(self, title):
        self.database.execute("DELETE FROM books WHERE title = %s",(title,),which_query='w')
        return "Book has been removed successfully."
    
    def register_member(self, name, member_id,join_date,database):
        join_date = date.today()
        member = Member(self,name, member_id,join_date, database)
        self.members.append(member)
        print(f'{member.name} was registered.')
        [first_name, last_name] = name.split(" ")
        self.database.execute(f"""
        INSERT INTO library_members (first_name, last_name, join_date)
        VALUES ('{first_name}', '{last_name}', '{join_date}');
        """)
        
    
    def borrow_book(self, member_id, title,):
        
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

        database.execute("""
        INSERT INTO borrowed_books (title,member_id)
        VALUES (%s,%s);
        """,(title,member_id,))
        
        

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


