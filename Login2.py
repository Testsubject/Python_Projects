import tkinter

main = tkinter.Tk()
main.title('Login')
main.geometry('200x150')

def new_user():
    window = tkinter.Toplevel(main)
    window.geometry('200x150')

    new_user = tkinter.Label(window, text='Enter a new username')
    new_userE = tkinter.Entry(window)
    new_user.pack()
    new_userE.pack()
    new_username = new_userE.get()

    new_pas = tkinter.Label(window, text='Enter a new password')
    new_pasE = tkinter.Entry(window)
    new_pas.pack()
    new_pasE.pack()
    new_password = new_pasE.get()

    confirm = tkinter.Button(window, text='Confirm', command=window.destroy)
    confirm.pack()

def check():
    if(username == new_username and password == new_password):
        print('test')

user = tkinter.Label(main, text='Username')
userE = tkinter.Entry(main)
user.pack()
userE.pack()
username = userE.get()

pas = tkinter.Label(main, text='Password')
pasE = tkinter.Entry(main, show='*')
pas.pack()
pasE.pack()
password = pasE.get()

new = tkinter.Button(main, text='Create new', command=new_user)
new.pack()

but = tkinter.Button(main, text='Login', command=check)
but.pack()

main.mainloop()
