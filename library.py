import psycopg2
class database:
   def __init__(self):
    self.conn = psycopg2.connect(
        PGDATABASE = "railway",
        PGHOST = "containers-us-west-22.railway.app",
        PGPASSWORD = "DW0OLFxKHv65MjGdtUY4",
        PGPORT = "5760",
        PGUSER = "postgres"
        )
    self.cur = conn.cursor()
    def execute(self,query,PARAM=None,which_query='r'):
        try:
            self.cursor.execute(query,PARAM)
        except:
            print('Oops..something went wrong.',query)
        finally:
            if which_query=='r':
                print(cur.fetchall())
            if which_query=='w':
               conn.commit()
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
        try:   
    
    
    def borrow_book(self, book):
        if book.status == 'available':
            book.status = 'borrowed'
            self.borrowed_books.append(book)
            print(f'{self.name} borrowed {book.title}.')
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


class Library:
    def __init__(self):
        self.catalog = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.catalog.append(book)
        print(f'{book.title} was added to the catalog.')

    def remove_book(self, title):
        for book in self.catalog:
            if book.title == title:
                self.catalog.remove(book)
                print(f'{book.title} was removed from the catalog.')
                return
        print(f'Book not found.')

    def register_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f'{member.name} was registered.')

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

