import sqlite3
con=sqlite3.connect('aec1.db')
cur =con.cursor()
cur.execute('''create table ece(id integer primary key ,name text,age integer)''')
cur.execute("insert into ece(name,age) values (?,?)" , ('MOHIT',35))
