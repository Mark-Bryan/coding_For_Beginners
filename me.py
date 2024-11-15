from tkinter import *
from tkinter import messagebox, simpledialog
import os


def save_user_info():
    first_name = fnEntry.get()
    last_name = lnEntry.get()
    date_of_birth = dbEntry.get()
    password = pdEntry.get()
    confirm_password = confirmpdEntry.get()
    file_to_save = "user_information.txt"

    # Check if passwords match
    if password != confirm_password:
        messagebox.showwarning('Error', "Passwords do not match.")
        return

    # Save user info to file
    with open(file_to_save, 'w') as user_file:
        user_file.write(f'First Name: {first_name}\n')
        user_file.write(f"Last Name: {last_name}\n")
        user_file.write(f"Date Of Birth: {date_of_birth}\n")
        user_file.write(f"User Password: {password}\n")

    messagebox.showinfo("Success", 'Information has been saved successfully')


def retrieve_user_info():
    file_to_save = "user_information.txt"
    if os.path.exists(file_to_save):
        # Prompt user to enter their password
        entered_password = simpledialog.askstring("Password Required", "Enter your password:", show='*')
        
        if not entered_password:
            return  # If no password entered, just return

        # Read saved user information
        user_info = {}
        with open(file_to_save, 'r') as user_file:
            for line in user_file:
                key, value = line.strip().split(': ', 1)
                user_info[key] = value

        # Check if entered password matches saved password
        if entered_password == user_info.get("User Password"):
            messageTitle = f"{user_info['First Name']} {user_info['Last Name']}'s Account"
            messageContent = f"Account found for {user_info['First Name']} {user_info['Last Name']}\n" \
                             f"Date of Birth: {user_info['Date Of Birth']}"
            messagebox.showinfo(messageTitle, messageContent)
        else:
            messagebox.showerror('Error', "Access Denied due to wrong password.")
    else:
        messagebox.showerror('Error', 'No user information has been found.')


# GUI Setup
mainWindow = Tk()
mainWindow.title('User Registration App')

instructions = Label(mainWindow, text='Complete the form and press submit to register a new user')
instructions.pack(padx=20, pady=10)

# First Name
fnFrame = Frame(mainWindow)
fnlabel = Label(fnFrame, text="First Name")
fnEntry = Entry(fnFrame)

fnEntry.pack(side=RIGHT)
fnlabel.pack(side=LEFT)
fnFrame.pack(padx=20, pady=10)

# Last Name
lnFrame = Frame(mainWindow)
lnlabel = Label(lnFrame, text="Last Name")
lnEntry = Entry(lnFrame)

lnEntry.pack(side=RIGHT)
lnlabel.pack(side=LEFT)
lnFrame.pack(padx=20, pady=10)

# Date of Birth
dbFrame = Frame(mainWindow)
dblabel = Label(dbFrame, text="Date Of Birth")
dbEntry = Entry(dbFrame)

dbEntry.pack(side=RIGHT)
dblabel.pack(side=LEFT)
dbFrame.pack(padx=20, pady=10)

# Password
pdFrame = Frame(mainWindow)
pdlabel = Label(pdFrame, text="Password")
pdEntry = Entry(pdFrame, show="*")

pdEntry.pack(side=RIGHT)
pdlabel.pack(side=LEFT)
pdFrame.pack(padx=20, pady=10)

# Confirm Password
confirmpdFrame = Frame(mainWindow)
confirmpdlabel = Label(confirmpdFrame, text='Confirm your password')
confirmpdEntry = Entry(confirmpdFrame, show='*')

confirmpdEntry.pack(side=RIGHT)
confirmpdlabel.pack(side=LEFT)
confirmpdFrame.pack(padx=20, pady=10)

# Action Buttons Frame
actionsFrame = Frame(mainWindow)

save_button = Button(actionsFrame, text='Save Your Information', command=save_user_info)
save_button.pack(side=RIGHT, pady=10)

retrieve_button = Button(actionsFrame, text='Retrieve Your Information', command=retrieve_user_info)
retrieve_button.pack(side=LEFT, pady=10)
actionsFrame.pack(padx=10, pady=10)

mainWindow.mainloop()

