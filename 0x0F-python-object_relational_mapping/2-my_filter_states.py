#!/usr/bin/python3
'''displays all values in the states table of hbtn_0e_0_usa where name
matches the argument.'''
import MySQLdb
import sys


connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             port=3306)

cursor = connection.cursor()
cursor.execute("SELECT * FROM states")
rows = cursor.fetchall()

for row in rows:
    if row[1] == sys.argv[4]:
        print(row)

cursor.close()
connection.close()
