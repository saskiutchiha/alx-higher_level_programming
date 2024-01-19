#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
        conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],passwd=argv[2], db=argv[3], charset="utf8")
        cur = conn.cursor()
        cur.execute("select cities.id,cities.name,state.name from cities,state where state.id = cities.stat_id")
        query_rows = cur.fetchall()
        for row in query_rows:
                print(row)
        cur.close()
        conn.close()
