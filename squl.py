import mysql.connector

con=mysql.connector.connect(user='AROMAL.P',host='localhost',password='aromal@123',database='data7')
cur=con.cursor()
con.autocommit=True
# cur.execute("create database data7")
# cur.execute("create table std (roll int,name text,age int)")
roll=int(input("enter roll"))
name=str(input('enter name'))
age=int(input("enter age"))
cur.execute("insert into std(roll,name,age)values(%s,%s,%s)",(roll,name,age))
