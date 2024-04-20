#!/usr/bin/python3

import sys
import getpassi     # Secure way to prompt for password
import MySQLdb


def list_states(username, password, database):
    """Connects to a MySQL database, retrieves states (ordered by ID),
       and displays them.

    Args:
        username (str): Username for the MySQL database.
        password (str): Password (prompted securely).
        database (str): Name of the database to connect to.

    Raises:
        MySQLdb.Error: If database connection or query fails.
    """

    try:
        # Securely prompt for password if not provided
        if not password:
            password = getpass.getpass("Enter password: ")

        # Connect to MySQL server (localhost, port 3306)
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=username, passwd=password, db=database)
        cursor = conn.cursor()

        # Execute query to select all states, ordered by ID (ascending)
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cursor.fetchall()

        # Display results (consider formatting for better readability)
        print("List of states:")
        for state in states:
            print(state)  # You can customize the output format here

    except MySQLdb.Error as err:
        print(f"Error connecting to database: {err}")

    finally:
        # Ensure proper resource management (close cursor & connection)
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <database>")
        sys.exit(1)

    username = sys.argv[1]
    database = sys.argv[2]

    list_states(username, None, database)
