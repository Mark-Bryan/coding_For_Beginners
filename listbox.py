# from tkinter import*
# import tkinter.messagebox as box

# window = Tk()
# window.title('Listbox Example')

# frame = Frame(window)

# listbox = Listbox(frame)
# listbox.insert(1, 'HTML in easy steps')
# listbox.insert(2, 'CSS in easy steps')
# listbox.insert(3, 'JavaScript in easy steps')

# def dialog():
#     box.showinfo('Selection', 'Your choice:' +\
#                  listbox.get(listbox.curselection()) )
    
# btn = Button(frame, text='Choose', command= dialog)

# btn.pack(side=RIGHT, padx=5)
# listbox.pack(side=LEFT)
# frame.pack(padx=30, pady=30)

# window.mainloop()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily["child2"]["name"])

a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}

print(customers['c2']['name'])