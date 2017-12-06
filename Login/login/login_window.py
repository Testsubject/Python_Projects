#!/usr/bin/python

from tkinter import *

class LoginWindow(Frame):
    @classmethod
    def start(cls):
        main = Tk()
        main.title('Login')
        main.geometry('200x150')
        app = LoginWindow(main)
        app.mainloop()

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.shadows = {'default': 'password'}
        self._config_layout()

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if self.shadows.get(username) == password:
            print('You logged in')
        else:
            print('Wrong')

    def _config_layout(self):
        self.pack()

        Label(self, text='Username').pack()
        self.username_entry = Entry(self)
        self.username_entry.pack()

        Label(self, text='Password').pack()
        self.password_entry = Entry(self)
        self.password_entry.pack()

        Button(self, text='Login', command=self.login).pack()
