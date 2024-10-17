import tkinter

win=tkinter.Tk()
win.title=('Login')
win.configure(bg='green')
win.minsize(400,400)
win.maxsize(500,500)


def save():
    win1=tkinter.Tk()
    win1.title('Register')
    win1.configure(bg='yellow')
    win1.minsize(400,400)
    win1.maxsize(500,500)
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
    btn2=tkinter.Button(win1,text='submit',bg='gray',activebackground='green',activeforeground='white',padx=3,pady=3)
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


btn=tkinter.Button(win,text='submit',bg='gray',activebackground='black',activeforeground='white',padx=3,pady=3,)
btn.place(x=200,y=200)
btn1=tkinter.Button(win,text='register',bg='gray',activebackground='green',activeforeground='black',padx=3,pady=3,command=save)
btn1.place(x=50,y=250)


win.mainloop()
