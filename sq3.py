import sqlite3
con= sqlite3.connect("batch7.db")

try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass

# con.execute("insert into std(roll_no,name ,age)values(2,'akhil',22),(3,'sabu',43),(4,'yadhu',32)")
# con.commit()

roll=int(input('enter roll num'))
name=str(input('enter name'))
age=int(input('enter age'))

con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
con.commit()