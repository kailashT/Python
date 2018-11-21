
from tkinter import *


window = Tk()

window.title("Welcome to LikeGeeks app")
lbl2 = Label(window, text="Hello")
lbl2.grid(column=0, row=5)
window.geometry('350x200')

lbl = Label(window, text="Hello", font=("Arial Bold", 25))
lbl.grid(column=0, row=0)

#txt = Entry(window, width=10,state='disabled')
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
# txt.focus()


def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)


btn = Button(window, text="Click Me", command=clicked, bg="red", fg="yellow")
btn.grid(column=2, row=0)


window.mainloop()
