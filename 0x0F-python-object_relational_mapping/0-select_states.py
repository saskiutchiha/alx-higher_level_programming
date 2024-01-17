#!/usr/bin/python3
"""
This script lists all states from a MySQL database.

The script connects to a MySQL database using the provided command line arguments,
executes a SQL query to fetch all states ordered by their ID, and prints the result.

Command line arguments:
    1. MySQL username
    2. MySQL password
    3. MySQL database name

Dependencies:
    - MySQLdb: A Python DB API-2.0-compliant interface to MySQL.
    - sys: Provides access to some variables used or maintained by the Python interpreter.

Usage:
    python3 script.py <username> <password> <database>
"""

import MySQLdb as my
import sys 

# Parse command line arguments
a = sys.argv()

# Connect to the MySQL database
db = my.connect(host="localhost", port=3306, user=a[0], passwd=a[1], db=a[2])

# Create a cursor object
cursor = db.cursor()

# Execute SQL query
cursor.execute("select * from states order by states.id")

# Fetch and print all rows from the query
for data in cursor :
        print(data)

# Close the cursor and the database connection
cursor.close()
db.close()

