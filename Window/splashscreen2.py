from PIL import Image, ImageTk
from tkinter import *

image_path = "ironman.jpg"

root = Tk()
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*1, height*1, width*0, height*0))

image = Image.open(image_path)
image = image.resize((width, height), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas = Canvas(root, height=height*1, width=width*1, bg="darkgrey")
canvas.create_image(width*1/2, height*1/2, image=image)
canvas.pack()
root.after(5000, root.destroy)
root.mainloop()