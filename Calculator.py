import tkinter

main = tkinter.Tk()
main.title("Calculator")
main.geometry('255x100')
main.configure(background='#a1dbcd')

def add():
    total = int(e1.get()) + int(e2.get())
    print('Answer = %s' % total)

def subtract():
    total2 = int(e1.get()) - int(e2.get())
    print('Answer = %s' % total2)

def multiply():
    total3 = int(e1.get()) * int(e2.get())
    print('Answer = %s' % total3)

def divide():
    total4 = int(e1.get()) / int(e2.get())
    print('Answer = %s' % total4)


tkinter.Label(main, text='1st number', bg='#a1dbcd').place(x=0, y=2)
tkinter.Label(main, text='2nd number', bg='#a1dbcd').place(x=0, y=20)
e1 = tkinter.Entry(main)
e1.place(x=90, y=2)
e2 = tkinter.Entry(main)
e2.place(x=90, y=20)
tkinter.Button(main, text='Add', command=add).place(x=2, y=50)
tkinter.Button(main, text='Subtract', command=subtract).place(x=55, y=50)
tkinter.Button(main, text='Multiply', command=multiply).place(x=130, y=50)
tkinter.Button(main, text='Divide', command=divide).place(x=210, y=50)


main.mainloop()
