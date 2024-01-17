#!/usr/bin/python3
"lists all states"


import MySQLdb as my
import sys 
if __name__ == "__main__":
 a = sys.argv()
 db = my.connect(host="localhost", port=3306, user=a[1], passwd=a[2], db=a[3])
 cursor = db.cursor()
 cursor.execute("select * from states order by states.id;")
 for data in cursor :
    print(data)
 cursor.close()
 db.close()

