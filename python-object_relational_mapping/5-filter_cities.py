#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # Create a cursor
    cursor = db.cursor()

    # Prepare the query with placeholders and safely execute
    query = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()

    # Display the results
    if result and result[0]:
        print(result[0])

    # Close the cursor and connection
    cursor.close()
    db.close()
