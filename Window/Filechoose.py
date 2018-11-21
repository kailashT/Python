
from tkinter import filedialog
from tkinter import *


window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

def clicked():
    #file = filedialog.askopenfilename()
    file = filedialog.askopenfilenames()
    print(file)

btn = Button(window, text="Click Me", command=clicked , bg="red", fg="yellow")
btn.grid(column=0, row=0)


window.mainloop()
