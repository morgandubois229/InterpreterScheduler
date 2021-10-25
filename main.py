#Imports
from tkinter import *
import SQLQueries

##################################################
# Window Creation
##################################################

root = Tk()
root.title("Scheduler")
root.geometry('800x500')
instruction_label = Label(root, text='Current Instructions')
error_label = Label(root, text='Error Message')
current_connection = SQLQueries.create_connection()
current_username = ""

##################################################
# Helper Functions
##################################################

def clear_screen():
    for i in root.grid_slaves():
        i.grid_remove()

def exit_application():
    root.destroy()
    SQLQueries.close_connection(current_connection)
    exit()

##################################################
# Create Account
##################################################
def go_to_create_account():
    clear_screen()
    instruction_label.configure(text="How are you using this application?")
    instruction_label.grid(row=0, column=1, sticky="E")
    looking_for_button.grid(row=1, column=1, sticky="WE")
    interpreter_button.grid(row=2, column=1, sticky="WE")

def try_create_poster_account():
    clear_screen()
    # Implement code

def go_to_create_poster_account():
    clear_screen()
    # Implement code

def try_create_interpreter_account():
    clear_screen()
    # Implement code

def go_to_create_interpreter_account():
    clear_screen()
    first_name_entry.delete(0, 'end')
    middle_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    interpreter_ID_entry.delete(0, 'end')
    phone_number_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    instruction_label.configure(text="Please enter your information into the boxes. \nAll boxes with * are required")
    instruction_label.grid(row=0, column=0, columnspan=2)

    first_name_label.grid(row=1, column=0)
    middle_name_label.grid(row=2, column=0)
    last_name_label.grid(row=3, column=0)
    interpreter_ID_label.grid(row=4, column=0)
    phone_number_label.grid(row=5, column=0)
    email_label.grid(row=6, column=0)
    username_label.grid(row=7, column=0)
    password_label.grid(row=8, column=0)
    
    first_name_entry.grid(row=1, column=1)
    middle_name_entry.grid(row=2, column=1)
    last_name_entry.grid(row=3, column=1)
    interpreter_ID_entry.grid(row=4, column=1)
    phone_number_entry.grid(row=5, column=1)
    email_entry.grid(row=6, column=1)
    username_entry.grid(row=7, column=1)
    password_entry.grid(row=8, column=1)
    
    submit_interpreter_account.grid(row=9, column=0)


first_name_input = ""
middle_name_input = ""
last_name_input = ""
interpreter_ID_input = ""
phone_number_input = ""
email_input = ""
username_input = ""
password_input = ""

first_name_label = Label(root, text="*First Name:")
middle_name_label = Label(root, text="Middle Name:")
last_name_label = Label(root, text="*Last Name:")
interpreter_ID_label = Label(root, text="*Interpreter ID:")
phone_number_label = Label(root, text="*Phone Number:")
email_label = Label(root, text="*Email:")
username_label = Label(root, text="*Username:")
password_label = Label(root, text="*Password:")

first_name_entry = Entry(root, textvariable=first_name_input)
middle_name_entry = Entry(root, textvariable=middle_name_input)
last_name_entry = Entry(root, textvariable=last_name_input)
interpreter_ID_entry = Entry(root, textvariable=interpreter_ID_input)
phone_number_entry = Entry(root, textvariable=phone_number_input)
email_entry = Entry(root, textvariable=email_input)
username_entry = Entry(root, textvariable=username_input)
password_entry = Entry(root, textvariable=password_input)

looking_for_button = Button(root, text="I am looking for interpreting services", command=go_to_create_poster_account)
interpreter_button = Button(root, text="I am an interpreter", command=go_to_create_interpreter_account)

submit_interpreter_account = Button(root, text="Submit", command=try_create_interpreter_account)
submit_poster_account = Button(root, text="Submit", command=try_create_poster_account)

##################################################
# Login
##################################################

def go_to_login():
    clear_screen()
    emailusername_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    instruction_label.configure(text="Log in using your email or username, or creat an account")
    instruction_label.grid(row=0, column=0)
    emailusername_label.grid(row=1, column=0)
    emailusername_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1)
    login_button.grid(row=3, column=1)
    create_account_button.grid(row=3, column=0)
    exit_button.grid(row=4, column=0, sticky="E")

def try_login():
    clear_screen()
    #Implement code

emailusername_input = ""
password_input = ""
emailusername_label = Label(root, text="Email/Username:")
password_label = Label(root, text="Password:")
emailusername_entry = Entry(root, textvariable=emailusername_input)
password_entry = Entry(root, textvariable=password_input)
login_button = Button(root, text="Login", command=try_login)
create_account_button = Button(root, text="Create Account", command=go_to_create_account)
exit_button = Button(root, text="Exit", command=exit_application)

##################################################
# Launch Program
##################################################

if __name__ == "__main__":
    go_to_login()
    root.mainloop()