from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import Error

load_dotenv()

DB_HOST = os.getenv('containers-us-west-62.railway.app')
DB_NAME = os.getenv('railway')
DB_USER = os.getenv('postgres')
DB_PASS = os.getenv('xsxLOBFrhBjsG75Fgjhn')
DB_PORT = os.getenv('7802')

try:
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    for row in result:
        print(row)
except(Exception, Error) as e:
    print("Error, cannot connect to PostgreSQL:", e)
finally:
    try:
        if connection:
            cursor.close()
            connection.close()
    except NameError:
        pass