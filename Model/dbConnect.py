import psycopg2
from psycopg2 import errors
'''
    Database Information: to be used to connect to the local database that was created inside of pgAdmin4
'''
host = "localhost"
database = "employee_management"
user = "postgres"
password = "35171"

def getEmps():

    try:
        # Establish the connection
        db = psycopg2.connect(
            host=host, 
            database=database, 
            user=user, 
            password=password
        )

        # Create a cursor object
        cursor = db.cursor()

        # Gather all of the employees from the db table
        cursor.execute(
            f'''
            SELECT * 
            FROM employees
            '''
        )

        # Fetch the results
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        db.close()

        return results

    except psycopg2.Error as error:
        print("Error connecting to PostgreSQL:", error)


def getAvailabilities():
    try:
        # Establish the connection
        db = psycopg2.connect(
            host=host, 
            database=database, 
            user=user, 
            password=password
        )

        # Create a cursor object
        cursor = db.cursor()

        # Gather all of the employees from the db table
        cursor.execute(
            f'''
            SELECT * 
            FROM availability
            '''
        )

        # Fetch the results
        results = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        db.close()

        return results

    except psycopg2.Error as error:
        print("Error connecting to PostgreSQL:", error)
