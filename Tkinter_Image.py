from tkinter import *

root = Tk()

photo = PhotoImage(file="Japan.ppm")
w = Label(root, image = photo)
w.image = photo
w.pack()

root.mainloop()