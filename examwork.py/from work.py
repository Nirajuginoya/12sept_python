import tkinter
from tkinter import ttk

screen=tkinter.Tk()
screen.geometry("800x700")
screen.config(bg='light green')
screen.title('new from')

tkinter.Label(text="firstname:",bg='lightgreen',fg='green',font='colour is blod').grid(row=0,column=1)
tkinter.Label(text="lastname:",bg='lightgreen',fg='green',font='colour is blod').grid(row=1,column=1)

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text='male',bg='highlight',fg='green',font='colour is bold').grid(row=2,column=2,sticky='W')
tkinter.Radiobutton(value=0,text='femal',bg='highlight',fg='green',font='colour is bold').grid(row=2,column=3,sticky='W')


