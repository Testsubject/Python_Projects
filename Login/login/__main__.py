#!/usr/bin/python

from login_window import LoginWindow

from tkinter import *

class NewUserWindow(Frame):
    def __init__(self, master, shadows):
        Frame.__init__(self, master)
        self.master = master

if __name__ == '__main__':
    LoginWindow.start()
