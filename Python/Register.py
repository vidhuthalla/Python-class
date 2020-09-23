from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Welcome To {INSERST NAME HERE}")
window.geometry('400x400')
window.configure(background = "grey")
fname = Label(window ,text = "First Name").grid(row = 0,column = 0)
lname = Label(window ,text = "Last Name").grid(row = 1,column = 0)
email = Label(window ,text = "Email ID").grid(row = 2,column = 0)
contact = Label(window ,text = "Contact").grid(row = 2,column = 0)
a = Entry(window).grid(row = 0,column = 1)
b = Entry(window).grid(row = 1,column = 1)
c = Entry(window).grid(row = 2,column = 1)
d = Entry(window).grid(row = 3,column = 1)
def clicked():
	res = "Welcome to " + txt.get()
	lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row = 4, column=0)
window.mainloop()