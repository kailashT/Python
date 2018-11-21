23
24
25
from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('350x200')

style = ttk.Style()

style.theme_use('default')

style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column=0, row=0)

var =IntVar()
var.set(36)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=0, row=2)

window.mainloop()