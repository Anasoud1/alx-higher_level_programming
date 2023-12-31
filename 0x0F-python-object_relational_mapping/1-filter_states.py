#!/usr/bin/python3
'''lists all states with a name starting with N (upper N) from the database
hbtn_0e_0_usa'''
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3],
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        if row[1][0] == "N":
            print(row)

    cursor.close()
    connection.close()
