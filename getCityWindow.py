from tkinter import *


def send():
    print("Print %s" % box.get())


def get():
    window = Toplevel()
    window.title("Get city")
    window.focus_force()
    window.grab_set()

    txt = Label(window, text="Insert the city")
    txt.grid(column=0, row=0, padx=10, pady=10)

    Label(window, text="Type here", anchor=W).grid(column=0, row=1, padx=10, pady=10)
    box = Entry(window)
    box.grid(column=0, row=2, padx=10, pady=10)
    

    send_button = Button(window, text="OK")
    send_button.grid(column=0, row=3, padx=10, pady=10)


