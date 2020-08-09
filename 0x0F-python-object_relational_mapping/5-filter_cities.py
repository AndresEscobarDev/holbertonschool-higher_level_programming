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
    cur.execute("SELECT cities.name\
                FROM cities LEFT JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (sys.argv[4],))
    count = 0
    for row in cur.fetchall():
        if count == 0:
            print(row[0], end="")
            count += 1
        else:
            print(", " + row[0], end="")
    print()
