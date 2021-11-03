# Imports
from tkinter import *

import DataHelper
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
current_email = ""


##################################################
# Helper Functions
##################################################

# Clears the screen of all tkinter objects
def clear_screen():
    for i in root.grid_slaves():
        i.grid_remove()


def go_to_login_wrapper():
    go_to_login()


def go_to_create_account_wrapper():
    go_to_create_account()


def go_to_job_poster_main_menu_wrapper():
    job_poster_main_menu()


# Closes the application
def exit_application():
    root.destroy()
    SQLQueries.close_connection(current_connection.cursor())
    exit()


# Checks to make sure that password is valid and meets requirements
def check_new_password(password):
    check = False
    # Check for too long password
    if (len(password) > 20):
        error_label.configure(text="Error, password too long\nPlease use less than 20 characters")
        return True

    # Check for capital letter
    for i in range(len(password)):
        print(i)
        if (password[i] > chr(64) and password[i] < chr(91)):
            check = True
            break
    if (not check):
        error_label.configure(text="Error, no capital letter\nPlease use at least 1 capital letter")
        return True
    check = False

    # Check for number
    for i in range(len(password)):
        if (password[i] > chr(47) and password[i] < chr(58)):
            check = True
            break
    if (not check):
        error_label.configure(text="Error, no number\nPlease use at least 1 number")
        return True

    return False


def validate_phone_number(number):
    print("Implement me!")


##################################################
# Create Account
##################################################
def go_to_create_account():
    clear_screen()
    instruction_label.configure(text="How are you using this application?")
    instruction_label.grid(row=0, column=1, sticky="E")
    looking_for_button.grid(row=1, column=1, sticky="WE")
    interpreter_button.grid(row=2, column=1, sticky="WE")
    return_to_login_button.grid(row=4, column=1, sticky="WE")


##################################################
# Create Account Job Poster
##################################################
def try_create_poster_account():
    global current_connection
    error_label.grid_remove()
    first_name_input = first_name_entry.get()
    middle_name_input = middle_name_entry.get()
    last_name_input = last_name_entry.get()
    email_input = email_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    phone_number_input = phone_number_entry.get()

    if (first_name_input == "" or last_name_input == "" or email_input == ""
            or password_input == ""):
        error_label.configure(text="Please fill out all \nrequired text boxes (*)")
        error_label.grid(row=10, column=1)
    elif (check_new_password(password_input)):
        error_label.grid(row=10, column=1)
        password_entry.delete(0, 'end')
    elif (len(first_name_input) > 20 or len(middle_name_input) > 20 or len(last_name_input) > 20 or len(
            email_input) > 40 or len(username_input) > 20):
        error_label.configure(text="Text entry too long\nPlease use a shorter entry")
        error_label.grid(row=10, column=1)
        if (len(first_name_input) > 20):
            first_name_entry.delete(0, 'end')
        if (len(middle_name_input) > 20):
            middle_name_entry.delete(0, 'end')
        if (len(last_name_input) > 20):
            last_name_entry.delete(0, 'end')
        if (len(email_input) > 20):
            email_entry.delete(0, 'end')
        if (len(username_input) > 20):
            username_entry.delete(0, 'end')
    elif (SQLQueries.check_for_job_poster_email(current_connection.cursor(), email_input)):
        error_label.configure(text="Email already in use\nPlease use a different email")
        email_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    elif (SQLQueries.check_for_job_poster_username(current_connection.cursor(), username_input)):
        error_label.configure(text="Username already in use\nPlease use a different username")
        username_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    # Validate Phone number
    elif (DataHelper.check_phone_number(phone_number_input) == ""):
        error_label.configure(text="Phone number format incorrect\nPlease verify phone number")
        phone_number_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    # Create Interpreter
    else:
        SQLQueries.add_job_poster_account(current_connection.cursor(), first_name_input, middle_name_input,
                                          last_name_input, phone_number_input, email_input,
                                          username_input, password_input)
        go_to_login_wrapper()


def go_to_create_poster_account():
    clear_screen()
    first_name_entry.delete(0, 'end')
    middle_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    phone_number_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    password_label = Label(root, text="*Password:")

    instruction_label.configure(text="Please enter your information into the boxes. \nAll boxes with * are required")
    instruction_label.grid(row=0, column=0, columnspan=2)

    first_name_label.grid(row=1, column=0)
    middle_name_label.grid(row=2, column=0)
    last_name_label.grid(row=3, column=0)
    phone_number_label.grid(row=4, column=0)
    email_label.grid(row=5, column=0)
    username_label.grid(row=6, column=0)
    password_label.grid(row=7, column=0)

    first_name_entry.grid(row=1, column=1)
    middle_name_entry.grid(row=2, column=1)
    last_name_entry.grid(row=3, column=1)
    phone_number_entry.grid(row=4, column=1)
    email_entry.grid(row=5, column=1)
    username_entry.grid(row=6, column=1)
    password_entry.grid(row=7, column=1)
    submit_poster_account.grid(row=8, column=1)
    return_to_choose_account_button.grid(row=8, column=0)


##################################################
# Create Account Interpreter
##################################################
def try_create_interpreter_account():
    global current_connection
    error_label.grid_remove()
    first_name_input = first_name_entry.get()
    middle_name_input = middle_name_entry.get()
    last_name_input = last_name_entry.get()
    interpreter_ID_input = interpreter_ID_entry.get()
    email_input = email_entry.get()
    username_input = username_entry.get()
    password_input = password_entry.get()
    phone_number_input = phone_number_entry.get()

    if (first_name_input == "" or last_name_input == "" or interpreter_ID_input == "" or email_input == ""
            or password_input == ""):
        error_label.configure(text="Please fill out all \nrequired text boxes (*)")
        error_label.grid(row=10, column=1)
    elif (check_new_password(password_input)):
        error_label.grid(row=10, column=1)
        password_entry.delete(0, 'end')
    elif (len(first_name_input) > 20 or len(middle_name_input) > 20 or len(last_name_input) > 20 or len(
            email_input) > 40 or len(username_input) > 20):
        error_label.configure(text="Text entry too long\nPlease use a shorter entry")
        error_label.grid(row=10, column=1)
        if (len(first_name_input) > 20):
            first_name_entry.delete(0, 'end')
        if (len(middle_name_input) > 20):
            middle_name_entry.delete(0, 'end')
        if (len(last_name_input) > 20):
            last_name_entry.delete(0, 'end')
        if (len(email_input) > 20):
            email_entry.delete(0, 'end')
        if (len(username_input) > 20):
            username_entry.delete(0, 'end')
    elif (SQLQueries.check_for_interpreter_email(current_connection.cursor(), email_input)):
        error_label.configure(text="Email already in use\nPlease use a different email")
        email_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    elif (SQLQueries.check_for_interpreter_username(current_connection.cursor(), username_input)):
        error_label.configure(text="Username already in use\nPlease use a different username")
        username_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    elif (SQLQueries.check_for_interpreter_ID(current_connection.cursor(), interpreter_ID_input)):
        error_label.configure(text="InterpreterID already in use\nPlease verify you have the correct ID entered")
        interpreter_ID_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    # Validate Phone number
    elif (DataHelper.check_phone_number(phone_number_input) == ""):
        error_label.configure(text="Phone number format incorrect\nPlease verify phone number")
        phone_number_entry.delete(0, 'end')
        error_label.grid(row=10, column=1)
    # Create Interpreter
    else:
        SQLQueries.add_interpreter_account(current_connection.cursor(), first_name_input, middle_name_input,
                                           last_name_input, interpreter_ID_input, phone_number_input, email_input,
                                           username_input, password_input)
        go_to_login_wrapper()


def go_to_create_interpreter_account():
    clear_screen()
    first_name_entry.delete(0, 'end')
    middle_name_entry.delete(0, 'end')
    last_name_entry.delete(0, 'end')
    interpreter_ID_entry.delete(0, 'end')
    phone_number_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    password_entry.delete(0, 'end')

    password_label = Label(root, text="*Password:")

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
    submit_interpreter_account.grid(row=9, column=1)
    return_to_choose_account_button.grid(row=9, column=0)


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

return_to_login_button = Button(root, text="Back", command=go_to_login_wrapper)
return_to_choose_account_button = Button(root, text="Back", command=go_to_create_account_wrapper)

looking_for_button = Button(root, text="I am looking for interpreting services", command=go_to_create_poster_account)
interpreter_button = Button(root, text="I am an interpreter", command=go_to_create_interpreter_account)

submit_interpreter_account = Button(root, text="Submit", command=try_create_interpreter_account)
submit_poster_account = Button(root, text="Submit", command=try_create_poster_account)


##################################################
# Post Job
##################################################
def go_to_post_job():
    clear_screen()
    post_job_zipcode_entry.delete(0, 'end')
    post_job_LEPNumber_entry.delete(0, 'end')
    post_job_claimnuber_entry.delete(0, 'end')
    # implement Payer
    # implement Language
    post_job_servicedate_entry.delete(0, 'end')
    post_job_checkintime_entry.delete(0, 'end')
    post_job_starttime_entry.delete(0, 'end')
    post_job_endtime_entry.delete(0, 'end')
    # implement priority level - internal or external?
    post_job_description_entry.delete(0, 'end')

    instruction_label.configure(text="Please enter job information")
    instruction_label.grid(row=0, column=1)

    post_job_street_label.grid(row=1, column=0)
    post_job_street2_label.grid(row=2, column=0)
    post_job_city_label.grid(row=3, column=0)
    # Implenent tate dropdown
    # Implement County dropdown
    post_job_zipcode_label.grid(row=4, column=0)
    post_job_LEPNumber_label.grid(row=5, column=0)
    post_job_claimnuber_label.grid(row=6, column=0)
    # implement Payer
    # implement Language
    post_job_servicedate_label.grid(row=7, column=0)
    post_job_checkintime_label.grid(row=8, column=0)
    post_job_starttime_label.grid(row=9, column=0)
    post_job_endtime_label.grid(row=10, column=0)
    # implement priority level - internal or external?
    post_job_description_label.grid(row=11, column=0)

    post_job_street_entry.grid(row=1, column=1)
    post_job_street2_entry.grid(row=2, column=1)
    post_job_city_entry.grid(row=3, column=1)
    # Implenent tate dropdown
    # Implement County dropdown
    post_job_zipcode_entry.grid(row=4, column=1)
    post_job_LEPNumber_entry.grid(row=5, column=1)
    post_job_claimnuber_entry.grid(row=6, column=1)
    # implement Payer
    # implement Language
    post_job_servicedate_entry.grid(row=7, column=1)
    post_job_checkintime_entry.grid(row=8, column=1)
    post_job_starttime_entry.grid(row=9, column=1)
    post_job_endtime_entry.grid(row=10, column=1)
    # implement priority level - internal or external?
    post_job_description_entry.grid(row=11, column=1)

    post_job_main_menu_button.grid(row=12, column=0)
    post_job_submit_button.grid(row=12, column=1)


def try_post_job():
    global current_connection
    global current_email
    post_job_street_input = post_job_street_entry.get()
    post_job_street2_input = post_job_street2_entry.get()
    post_job_city_input = post_job_city_entry.get()
    # Implenent State dropdown
    # Implement County dropdown
    post_job_zipcode_input = post_job_zipcode_entry.get()
    post_job_LEPNumber_input = post_job_LEPNumber_entry.get()
    post_job_claimnuber_input = post_job_claimnuber_entry.get()
    # implement Payer
    # implement Language
    post_job_servicedate_input = post_job_servicedate_entry.get()
    post_job_checkintime_input = post_job_checkintime_entry.get()
    post_job_starttime_input = post_job_starttime_entry.get()
    post_job_endtime_input = post_job_endtime_entry.get()
    # implement priority level - internal or external?
    post_job_description_input = post_job_description_entry.get()

    SQLQueries.create_job(current_connection.cursor(), post_job_street_input, post_job_street2_input,
                          post_job_city_input, post_job_zipcode_input, post_job_LEPNumber_input,
                          post_job_claimnuber_input, post_job_servicedate_input, post_job_checkintime_input,
                          post_job_starttime_input, post_job_endtime_input, post_job_description_input, current_email)

    go_to_job_poster_main_menu_wrapper()


post_job_street_input = ""
post_job_street2_input = ""
post_job_city_input = ""
# Implenent State dropdown
# Implement County dropdown
post_job_zipcode_input = ""
post_job_LEPNumber_input = ""
post_job_claimnuber_input = ""
# implement Payer
# implement Language
post_job_servicedate_input = ""
post_job_checkintime_input = ""
post_job_starttime_input = ""
post_job_endtime_input = ""
# implement priority level - internal or external?
post_job_description_input = ""

post_job_street_label = Label(root, text="Street:")
post_job_street2_label = Label(root, text="Street:")
post_job_city_label = Label(root, text="City:")
# Implenent tate dropdown
# Implement County dropdown
post_job_zipcode_label = Label(root, text="Zipcode:")
post_job_LEPNumber_label = Label(root, text="LEP Number:")
post_job_claimnuber_label = Label(root, text="Claim Number:")
# implement Payer
# implement Language
post_job_servicedate_label = Label(root, text="Service Date:")
post_job_checkintime_label = Label(root, text="Check in Time:")
post_job_starttime_label = Label(root, text="Start Time:")
post_job_endtime_label = Label(root, text="End Time:")
# implement priority level - internal or external?
post_job_description_label = Label(root, text="Description:")

post_job_street_entry = Entry(root, textvariable=post_job_street_input)
post_job_street2_entry = Entry(root, textvariable=post_job_street2_input)
post_job_city_entry = Entry(root, textvariable=post_job_city_input)
# Implenent tate dropdown
# Implement County dropdown
post_job_zipcode_entry = Entry(root, textvariable=post_job_zipcode_input)
post_job_LEPNumber_entry = Entry(root, textvariable=post_job_LEPNumber_input)
post_job_claimnuber_entry = Entry(root, textvariable=post_job_claimnuber_input)
# implement Payer
# implement Language
post_job_servicedate_entry = Entry(root, textvariable=post_job_servicedate_input)
post_job_checkintime_entry = Entry(root, textvariable=post_job_checkintime_input)
post_job_starttime_entry = Entry(root, textvariable=post_job_starttime_input)
post_job_endtime_entry = Entry(root, textvariable=post_job_endtime_input)
# implement priority level - internal or external?
post_job_description_entry = Entry(root, textvariable=post_job_description_input)

post_job_main_menu_button = Button(root, text="Main Menu", command=go_to_job_poster_main_menu_wrapper)
post_job_submit_button = Button(root, text="Post Job", command=try_post_job)


##################################################
# Job Poster Jobs
##################################################
def go_to_my_jobs_job_poster():
    clear_screen()
    # implement code


##################################################
# Job Poster Invoices
##################################################
def go_to_my_invoices_job_poster():
    clear_screen()
    # implement code


##################################################
# Job Poster Main Menu
##################################################
def job_poster_main_menu():
    global current_email
    clear_screen()
    instruction_label.configure(text="Job Poster Main Menu")
    instruction_label.grid(row=0, column=0, sticky="WE")
    main_menu_job_poster_post_job_button.grid(row=1, column=0, sticky="WE")
    main_menu_job_poster_view_jobs_button.grid(row=2, column=0, sticky="WE")
    main_menu_job_poster_view_invoices_buttons.grid(row=3, column=0, sticky="WE")
    main_menu_job_poster_logout_button.grid(row=4, column=0, sticky="WE")


main_menu_job_poster_post_job_button = Button(root, text="Post Job", command=go_to_post_job)
main_menu_job_poster_view_jobs_button = Button(root, text="View My Jobs", command=go_to_my_jobs_job_poster)
main_menu_job_poster_view_invoices_buttons = Button(root, text="View My Invoices", command=go_to_my_invoices_job_poster)
main_menu_job_poster_logout_button = Button(root, text="Logout", command=go_to_login_wrapper)


##################################################
# Interpreter Main Menu
##################################################
def interpreter_main_menu():
    clear_screen()
    instruction_label.configure(text="Job Poster Main Menu")
    instruction_label.grid(row=0, column=0)
    # implement code


##################################################
# Login
##################################################

def go_to_login():
    clear_screen()
    login_emailusername_entry.delete(0, 'end')
    login_password_entry.delete(0, 'end')
    instruction_label.configure(text="Log in using your email or username, or creat an account")
    instruction_label.grid(row=0, column=0)
    login_emailusername_label.grid(row=1, column=0)
    login_emailusername_entry.grid(row=1, column=1)
    login_password_label.grid(row=2, column=0)
    login_password_entry.grid(row=2, column=1)
    login_login_button.grid(row=3, column=1)
    create_account_button.grid(row=3, column=0)
    login_exit_button.grid(row=4, column=0, sticky="E")


def try_login():
    global current_email
    login_emailusername_input = login_emailusername_entry.get()
    login_password_input = login_password_entry.get()
    result = SQLQueries.try_login(current_connection.cursor(), login_emailusername_input, login_password_input)
    print(result)
    if (result[0] == False):
        go_to_login()
    else:
        if (result[1] == "username"):
            current_email = SQLQueries.get_email_from_username(current_connection.cursor(), login_emailusername_input)
        else:
            current_email = login_emailusername_input
        if (result[2] == 0):
            job_poster_main_menu()
        else:
            interpreter_main_menu()


login_emailusername_input = ""
login_password_input = ""
login_emailusername_label = Label(root, text="Email/Username:")
login_password_label = Label(root, text="login_password:")
login_emailusername_entry = Entry(root, textvariable=login_emailusername_input)
login_password_entry = Entry(root, textvariable=login_password_input)
login_login_button = Button(root, text="Login", command=try_login)
create_account_button = Button(root, text="Create Account", command=go_to_create_account)
login_exit_button = Button(root, text="Exit", command=exit_application)

##################################################
# Launch Program
##################################################

if __name__ == "__main__":
    go_to_login()
    root.mainloop()
