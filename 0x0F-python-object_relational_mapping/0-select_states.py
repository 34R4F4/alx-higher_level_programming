#!/usr/bin/python3

import sys
import MySQLdb


def list_states(username, password, database):
    """Connects to a MySQL database, retrieves a list of states ordered by ID,
       and displays them.

    **Insecure for production!** Prompting for password directly exposes it.
    Consider environment variables or a secure configuration file.

    Args:
        username (str): Username for the MySQL database.
        password (str): Password for the MySQL database (prompted manually).
        database (str): Name of the database to connect to.

    Raises:
        MySQLdb.Error: If database connection or query fails.
    """

    try:
        # Connect to MySQL server (localhost, port 3306)
        conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username, 
                passwd=password, 
                db=database
                )
        cursor = conn.cursor()

        # Execute query to select all states, ordered by ID (ascending)
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cursor.fetchall()

        # Display results (consider formatting the output for readability)
        print("List of states:")
        for state in states:
            print(state)

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
    password = sys.argv[2]
    database = sys.argv[2]

    list_states(username, password, database)
