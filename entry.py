from tkinter import*
import tkinter.messagebox as box
window = Tk()
window.title('Entry Example')
Frame = Frame(window)
Entry = Entry(Frame)

def dialog():
    box.showinfo('Greetings', 'Welcome' + Entry.get())

btn = Button(Frame, text='Enter Name', command= dialog)
btn.pack(side = RIGHT, padx=5)
Entry.pack(side = LEFT)
Frame.pack(padx=20, pady=20)
window.mainloop()