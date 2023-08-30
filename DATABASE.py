import sqlite3

con=sqlite3.connect('MyDB')
cur=con.cursor()
cur.execute("create table if not exists operator(opid int primary key,name varchar(20),address varchar(30),email varchar(30),phone int);")
cur.execute("create table if not exists bus(bid text primary key,bus_type text,capacity integer,fare integer,rid text references route(rid),opid text references operator(opid));")
cur.execute("create table if not exists run(bid varchar(10),rdate date,available int);")
cur.execute("create table if not exists route(rid varchar(10),sid varchar(10),sname varchar(20));")
cur.execute("create table if not exists booking(book_ref int auto increament,name varchr(20),gender varchar(10),seats int,mobile int,email varchar(20),age int,bid varchar(10));")
cur.execute("select * from bus")
res=cur.fetchall()
print(res)
con.commit()


                                                      
