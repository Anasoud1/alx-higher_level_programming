#!/usr/bin/python3
'''displays all values in the states table of hbtn_0e_0_usa where name
matches the argument.'''
import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3],
                                 port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities "
                   "INNER JOIN states ON states.id = cities.state_id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
