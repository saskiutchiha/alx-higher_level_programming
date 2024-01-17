#!/usr/bin/python3
"lists all states"


import MySQLdb as my
import sys 
if __name__ == "__main__":
 a = sys.argv()
 db = my.connect(host="localhost", port=3306, user=a[0], passwd=a[1], db=a[2])
 cursor = db.cursor()
 cursor.execute("select * from states order by states.id")
 for data in cursor :
    print(data)
 cursor.close()
 db.close()

