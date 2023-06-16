from faker import Faker
import psycopg2
import random
from tqdm import tqdm

fake = Faker()

# Prompt user for database connection info
print("Enter database connection information:")
host = input("PGHOST: ")
port = input("PGPORT: ")
database = input("PGDATABASE: ")
user = input("PGUSER: ")
password = input("PGPASSWORD: ")

# Prompt user for rather or not to remove previous data
remove_data = input("Remove previous data? (y/n): ")

conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)

cur = conn.cursor()

# Remove previous data if user chooses to
if remove_data.lower() == 'y':
    cur.execute("""
    DROP TABLE IF EXISTS borrowed_books;
    DROP TABLE IF EXISTS books;
    DROP TABLE IF EXISTS library_members;
    """)


# Create tables

## Create table for Library Members
cur.execute("""
CREATE TABLE IF NOT EXISTS library_members (
    member_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    join_date DATE NOT NULL
)
""")

## Create table for Books
cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    status TEXT NOT NULL
) 
""")

## Create table for Borrowed Books
cur.execute("""
CREATE TABLE IF NOT EXISTS borrowed_books (
    borrow_id SERIAL PRIMARY KEY,
    member_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE NOT NULL
)
""")

# Insert data into tables

print("Seeding library_members...")
## Use a loop and faker data to seed 300 library_members
for _ in tqdm(range(300)):
    cur.execute("""
    INSERT INTO library_members (first_name, last_name, join_date)
    VALUES (%s, %s, %s)
    """, (fake.first_name(), fake.last_name(), fake.date_between(start_date='-5y', end_date='today')))

print("Seeding books...")
## Use a loop and faker data to seed 1000 books
for _ in tqdm(range(1000)):
    cur.execute("""
    INSERT INTO books (title, author, category, status)
    VALUES (%s, %s, %s, %s)
    """, (fake.sentence(nb_words=6, variable_nb_words=True), fake.name(), random.choice(['Fiction', 'Non-Fiction', 'Sci-Fi', 'Fantasy', 'Mystery', 'Thriller', 'Romance', 'Western', 'Dystopian', 'Memoir', 'Biography', 'Self-Help', 'Cookbook', 'History', 'Poetry', 'True Crime', 'Humor', 'Horror', 'Science', 'Art', 'Children']), random.choice(['Checked Out', 'Available'])))

## Use a loop and faker data to seed 250 borrowed_books
print("Seeding borrowed_books...")
for _ in tqdm(range(250)):
    borrow_date = fake.date_between(start_date='-5y', end_date='today')
    
    # Approximately 20% of the books are still borrowed
    if random.random() < 0.2:
        return_date = fake.date_between(start_date='today', end_date='+1y')
    else:
        return_date = fake.date_between(start_date=borrow_date, end_date='today')
        
    cur.execute("""
    INSERT INTO borrowed_books (member_id, book_id, borrow_date, return_date)
    VALUES (%s, %s, %s, %s)
    """, (random.randint(1, 300), random.randint(1, 1000), borrow_date, return_date))


# Commit changes. Close cursor and connection.
conn.commit()
cur.close()
conn.close()
