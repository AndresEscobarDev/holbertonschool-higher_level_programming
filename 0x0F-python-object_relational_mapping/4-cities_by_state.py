#!/usr/bin/python3
""" Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. """


if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states ON states.id = cities.state_id\
                ORDER BY id ASC;")
    for row in cur.fetchall():
        print(row)
