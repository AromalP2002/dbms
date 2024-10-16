import mysql.connector

con=mysql.connector.connect(user='AROMAL.P',host='localhost',password='aromal@123',database='data7')
cur=con.cursor()
con.autocommit=True
# cur.execute("create database data7")
# cur.execute("create table std (roll int,name text,age int)")
# roll=int(input("enter roll"))
# name=str(input('enter name'))
# age=int(input("enter age"))
# # cur.execute("insert into std (roll,name,age)values(%s,%s,%s)",(roll,name,age))
# cur.execute("insert into std (roll,name,age)values(%s,%s,%s)",(roll,name,age))

# cur.execute("select * from std std")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("select * from std where name like 'a%'")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("select * from std where name like '%a'")
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("create table mark(roll int,sub text,mark int)")

# cur.execute("insert into mark(roll,sub,mark)values(1,'cs',70),(1,'chem',49),(2,'phy',58),(4,'eng',45)")
# cur.execute("select std.roll,std.name,std.age,mark.sub,mark.mark from std cross join mark")
# data=cur.fetchall()
# for i in data:
#     print(i)
cur.execute('select name,count(age)from std group by name')
data=cur.fetchall()
for i in data:
    print(i)