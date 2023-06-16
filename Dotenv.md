# Using `dotenv` to Store Your Database Connection Details

To secure your application, sensitive details like database connection information should not be hard-coded into your application. Instead, these details can be stored securely using environment variables. The `python-dotenv` package is a Python module that allows you to specify environment variables in a .env file, improving the security and flexibility of your application.

Here are the steps to use `dotenv` in your Python application:

## Step 1: Installation

Install the `python-dotenv` package using pip. You can do this by running the following command in your terminal:

```bash
pip install python-dotenv
```

## Step 2: Create a `.env` File

Create a `.env` file in your project directory. This file will be used to store your environment variables. 

For example, your `.env` file might look something like this:

```bash
DB_HOST=localhost
DB_NAME=mydatabase
DB_USER=myusername
DB_PASS=mypassword
```

Remember, never commit your `.env` file to version control. Add `.env` to your `.gitignore` file to make sure it doesn't end up in your Git repository.

## Step 3: Load Environment Variables

You can now load these variables into your Python script using `dotenv`. Here's a basic example:

```python
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
```

With `dotenv`, you can easily manage sensitive information and configuration details without hard-coding them into your application.

## Step 4: Use Environment Variables in Database Connection

Now that you've loaded your environment variables, you can use them when connecting to your database. Here's an example using `psycopg2` to connect to a PostgreSQL database:

```python
import psycopg2
from psycopg2 import Error

try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query
    cursor.execute("SELECT * FROM books")

    # Fetch the result of the query
    result = cursor.fetchall()

    # Do something with the result
    for row in result:
        print(row)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Close the connection and cursor
    if (connection):
        cursor.close()
        connection.close()
```

In this script, the `psycopg2.connect()` function uses the environment variables loaded by `dotenv` to establish a connection to your PostgreSQL database. Once the connection is established, you can use the `cursor.execute()` function to execute SQL queries and `cursor.fetchall()` to fetch the results.

Remember, using `dotenv` is a best practice for handling sensitive information in your application. It keeps your configuration details separate from your code, making your application more secure and easier to manage.
