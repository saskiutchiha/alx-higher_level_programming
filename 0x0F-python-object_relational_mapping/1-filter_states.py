#!/usr/bin/python3
"lists all states"


import MySQLdb as my
from sys import argv
if __name__ == "__main__":

     db = my.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
     cursor = db.cursor()
     cursor.execute("select * from states where name like 'N%'order by states.id;")
     for data in cursor :
                print(data)
     cursor.close()
     db.close()
