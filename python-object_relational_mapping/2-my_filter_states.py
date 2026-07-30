#!/usr/bin/python3
"""Lists all states matching a user-supplied name (vulnerable to SQL
injection, as demonstrated in the next task)."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    name = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(name))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
