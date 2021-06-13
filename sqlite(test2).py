import sqlite3
a=str(input())
con = sqlite3.connect("Personal informations.db")
cur = con.cursor()
x=cur.execute("SELECT wallet_currency FROM customers WHERE username ='"+a+"'")
l=()
for i in x:
    l=i+l
print(20000+l[0])
