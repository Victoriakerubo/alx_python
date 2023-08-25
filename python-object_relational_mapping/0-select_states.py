#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Getting arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Creating a connection
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Rest of your script...
