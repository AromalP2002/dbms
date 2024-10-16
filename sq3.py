import sqlite3
con= sqlite3.connect("batch7.db")

try:
    con.execute("create table std(roll_no int,name text,age int)")
except:
    pass

import sqlite3
con= sqlite3.connect("batch7.db")

try:
    con.execute("create table mark(roll_no int,sub text,mark int)")
except:
    pass

# con.execute("insert into std(roll_no,name ,age)values(2,'akhil',22),(3,'sabu',43),(4,'yadhu',32)")
# con.commit()

con.execute("insert into mark(roll_no,sub ,mark)values(1,'cs',75),(1,'che',70),(2,'cs',65),(4,'py',55)")
con.commit()

# roll=int(input('enter roll num'))

# name=str(input('enter name'))
# age=int(input('enter age'))

# con.execute("insert into std(roll_no,name,age)values(?,?,?)",(roll,name,age))
# con.commit()

# data=con.execute("select * from std where roll_no=2")
# # print(data)
# for i in data:
#     print(i)


# data=con.execute("select * from std where name= 'sabu'")
# for i in data:
#     print(i)

# roll_no=int(input('enter the roll_no'))
# data=con.execute("select * from std where roll_no=?",(roll_no,))
# for i in data:
#     print(i)

# con.execute("update std set name='abi',age=18 where name='ae'")
# con.commit()

# a=input("enter new name")
# b=input("enter the old name")
# con.execute("update std set name=? where name=?",(a,b))
# con.commit()
# roll_no=int(input('enter the roll no'))
# con.execute("delete from std where roll_no=? ",(roll_no,))
# con.commit()

# # data=con.execute("select * from std where name like 'a%' ")
# # for i in data:
# #     print(i)

# data=con.execute("select * from std order by name desc") #(desc is a attribute to set to descending order by default it works as ascending order)
# for i in data:
#      print(i)


