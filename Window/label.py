from tkinter import *

from tkinter import messagebox

from tkinter.ttk import *

def clicked():
    messagebox.showinfo('Message', 'text Enter : {}'.format(txt.get()))


def CB_clicked():
    messagebox.showinfo('Message', 'text Enter : {}'.format(combo.get()))

def E_clicked():
    window.destroy()
#    messagebox.showinfo('Message title', 'Message content')

x = 0
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('500x500')

# lbl = Label(window, text="Hello")
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=x)

txt = Entry(window,width=40)
# txt = Entry(window, width=40)
x = x+1
txt.grid(column=0, row=x)
txt.focus()
chk_state = BooleanVar()
chk_state.set(True) #set check state
chk = Checkbutton(window, text='Entry', var=chk_state)
chk.grid(column=1, row=x)

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Text")
combo.current(1) # set the selected item
x = x+1
combo.grid(column=0, row=x)


# btn = Button(window, text="Click Me", command=clicked, bg="orange", fg="red")
btn = Button(window, text="Click Me", command=clicked)
x = x+1
btn.grid(column=0, row=x)

btn = Button(window, text="ComboBox", command=CB_clicked)
x = x+1
btn.grid(column=0, row=x)

btn = Button(window, text="Exit", command=E_clicked)
x = x+1
btn.grid(column=0, row=x)

window.mainloop()
