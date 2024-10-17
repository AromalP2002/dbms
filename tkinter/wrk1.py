import tkinter


win=tkinter.Tk()
win.title("batch7")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(500,500)
def save():
    



l1=tkinter.Label(win,text="LOGIN",bg="red",fg="black")
# l1.place(x=250,y=50)
l1.pack()

l2=tkinter.Label(win,text="uname")
l2.place(x=150,y=50)

e1=tkinter.Entry(win)
e1.place(x=250,y=50)

l3=tkinter.Label(win,text="Password")
l3.place(x=150,y=100)

e2=tkinter.Entry(win)
e2.place(x=250,y=100)

btn1=tkinter.Button(win,text="LOGIN",bg="grey",activebackground='black',activeforeground='white',padx=10,pady=8,command=save)






win.mainloop()