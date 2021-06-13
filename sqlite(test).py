import sqlite3
a=str(input())
#b="'"+a+"'"
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
b=cur.execute(" SELECT password FROM customers WHERE username = " + a)
for i in b:
    print(i)
