from tkinter import *
from tkinter import ttk
from tkinter import messagebox

web= Tk()
web.title('registration form')
web.geometry('480x450')
web.configure(bg='slate grey')

l0 = Label(web,text='registration form',width=20,bg='black')
l0.place(x=155,y=60)

l1 = Label(web,text='Full Name', width=13,bg='black')
l1.place(x=70,y=130)

e1 = Entry(web,bg='white',fg='black')
e1.place(x=240,y=130)

l2 = Label(web,text='Email',width=13,bg='black')
l2.place(x=70,y=180)

e2 = Entry(web,bg='white',fg='black')
e2.place(x=240,y=180)

l3=Label(web,text='Number',width=13,bg='black')
l3.place(x=70,y=230)

e3 = Entry(web,bg='white',fg='black')
e3.place(x=240,y=230)

l4=Label(web,text='Country',width=13,bg='black')
l4.place(x=70,y=280)

e4 = Entry(web,bg='white',fg='black')
e4.place(x=240,y=280)

def Button1():
    e1_value = e1.get()
    e2_value = e2.get()
    e3_value = e3.get()
    e4_value = e4.get()
    messagebox.showinfo('your information', f'Full Name: {e1_value}\nEmail: {e2_value}\nNumber: {e3_value}\nCountry: {e4_value}')

FB1 = Frame(web)
FB1.place(x=180,y=350)
B1 = ttk.Button(FB1,text='Submit',command=Button1)
B1.pack()

web.mainloop()

