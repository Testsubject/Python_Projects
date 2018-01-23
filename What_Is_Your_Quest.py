from tkinter import *
import tkinter

def show_entry_fields():
  print("Ah, so your name is %s, and your quest is %s. YOU FAIL IN YOUR QUEST!" % (e1.get(), e2.get()))


window = Tk()
window.title("Quest?")

Label(window, text="What is your name?").grid(row=0)
Label(window, text="What is your quest?").grid(row=1)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
