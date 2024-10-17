import tkinter

win=tkinter.Tk()
win.title("batch7")
win.configure(bg="green")
win.minsize(400,400)
win.maxsize(500,500)
def save():
    # print(e1.get())
    l3.config(text=e1.get())
    

l1=tkinter.Label(win,text="welcome to all",bg='red',fg='black')
# l1.pack()
l1.place(x=150,y=20)
# l1.grid(row=0,column=0)
# l2=tkinter.Label(win,text="welcome to all")
# l2.grid(row=10,column=2)
l2=tkinter.Label(win,text="name")
l2.place(x=75,y=50)

e1=tkinter.Entry(win)
e1.place(x=150,y=50)

btn1=tkinter.Button(win,text="save",bg="grey",activebackground="black",activeforeground="white",padx=10,pady=8,command=save)
btn1.place(x=150,y=75)

l3=tkinter.Label(win)
l3.place(x=150,y=120)







win.mainloop()