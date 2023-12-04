import sqlite3

dbcon=sqlite3.connect("newdb.db")

tbl_create="create table studinfo(id integer primary key autoincrement,name text ,city text)"
try:
   dbcon.execute(tbl_create)
   print("Table create succesfully!")
except Exception as e:
   print(e)

insert_data="insert into studinfo(name,city) values('niraju','rajkot')('hardik','baroda')('ravi','dhoraji')"
try:
   dbcon.execute(insert_data)
   dbcon.commit()
   print("reord inserted")

except Exception as e:
   print(e)     
      