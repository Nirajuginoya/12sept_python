import tkinter
from tkinter import ttk
from tkinter import messagebox

screen=tkinter.Tk()
screen.geometry("600x400")
screen.config(bg='light green')
screen.title('new from')

tkinter.Label(text="Firstnumber:",bg='light green',fg='green',font='Courier 15 bold').grid(row=0,column=0)
tkinter.Label(text="secondnumber:",bg='light green',fg='green',font='Courier 15 bold').grid(row=1,column=0)


txtfnm=tkinter.Entry()
txtfnm.grid(row=0,column=1,sticky='W')
txtsnm=tkinter.Entry()
txtsnm.grid(row=1,column=1,sticky='W')

tkinter.Button(text="add",bg='light green',fg='green',font='Courier 15 bold').grid(row=2,column=0,sticky='W')
tkinter.Button(text="sub",bg='light green',fg='green',font='Courier 15 bold').grid(row=4,column=0,sticky='W')
tkinter.Button(text="mul",bg='light green',fg='green',font='Courier 15 bold').grid(row=6,column=0,sticky='W')
tkinter.Button(text="div",bg='light green',fg='green',font='Courier 15 bold').grid(row=8,column=0,sticky='W')

def btnclick():
     
     print("Firstnumber:",txtfnm.get())
     print("Secondnumber:",txtsnm.get())


     messagebox.showinfo("Studetdata",f"Firstname:{txtfnm.get()} and Lastname:{txtsnm.get()}")

tkinter.mainloop()