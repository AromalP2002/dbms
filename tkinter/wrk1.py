import tkinter
import sqlite3
# con=sqlite3.connect("tkinter_data.db")
# con.execute("create table sample(uname text,password text)")
win=tkinter.Tk()
win.title=('Login')
win.configure(bg='green')
win.minsize(400,400)
win.maxsize(500,500)
def Home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text="Home Page",bg='green',fg="blue")
    l1.place(x=150,y=20)
    btn1=tkinter.Button(win2,text="logout",command=win2.quit)
    btn1.place(x=200,y=0)
    win2.mainloop()

def login():
    con=sqlite3.connect("tkinter_data.db")
    data=con.execute("select * from sample")
    f=0
    for i in data:
        if i[0]==e1.get()and i[1]==e2.get():
            f=1
            Home()
    if f==0:
        l3.config(text="invaild uname or password")        


def reg_from():
    win1=tkinter.Tk()
    win1.title('Register')
    win1.configure(bg='yellow')
    win1.minsize(400,400)
    win1.maxsize(500,500)
    def reg():
        con=sqlite3.connect("tkinter_data.db")
        con.execute("insert into sample(uname,password)values(?,?)",(e3.get(),e4.get()))
        con.commit()
        win1.destroy()
    l4=tkinter.Label(win1,text='REGISTER',bg='cyan',fg='black')
    l4.pack()
    l5=tkinter.Label(win1,text='User Name')
    l5.place(x=75,y=50)
    l6=tkinter.Label(win1,text='Password')
    l6.place(x=75,y=100)
    e3=tkinter.Entry(win1)
    e3.place(x=170,y=50)
    e4=tkinter.Entry(win1)
    e4.place(x=170,y=100)
    btn2=tkinter.Button(win1,text='submit',bg='gray',activebackground='green',activeforeground='white',padx=3,pady=3,command=reg)
    btn2.place(x=200,y=200)
    win1.mainloop()

l1=tkinter.Label(win,text='LOGIN',bg='purple',fg='black')
l1.pack()

l2=tkinter.Label(win,text='User Name')
l2.place(x=75,y=50)

l3=tkinter.Label(win,text='Password')
l3.place(x=75,y=100)



e1=tkinter.Entry(win)
e1.place(x=170,y=50)

e2=tkinter.Entry(win)
e2.place(x=170,y=100)


btn=tkinter.Button(win,text='submit',bg='gray',activebackground='black',activeforeground='white',padx=3,pady=3,command=login)
btn.place(x=200,y=200)
btn1=tkinter.Button(win,text='register',bg='gray',activebackground='green',activeforeground='black',padx=3,pady=3,command=reg_from)
btn1.place(x=50,y=250)


win.mainloop()
