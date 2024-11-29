from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title("Check Button Example")

frame = Frame(window)

var_1 = BooleanVar()
var_2 = BooleanVar()
var_3 = BooleanVar()

book_1 = Checkbutton(frame, text="HTML", variable=var_1)
book_2 = Checkbutton(frame, text="CSS", variable=var_2)
book_3 = Checkbutton(frame, text="JS", variable=var_3)


def dialog():
    s = "Your Choice"
    if var_1.get() == 1:
        s += "\nHTML in easy steps"
    if var_2.get() == 1:
        s += "\nCSS in easy steps"
    if var_3.get() == 1:
        s += "\nJavaScript in easy steps"
    box.showinfo("Selection", s)


btn = Button(frame, text="Choose", command=dialog)

btn.pack(side=RIGHT, padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()
