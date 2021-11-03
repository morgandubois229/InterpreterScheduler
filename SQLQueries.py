import psycopg2


def create_connection():
    scheduler_connection = psycopg2.connect(database="scheduler", user="postgres", password="cat123", host="127.0.0.1",
                                            port="5432")
    scheduler_connection.autocommit = True

    return scheduler_connection


def close_connection(current_connection):
    current_connection.close()


def check_for_interpreter_username(database_cursor, username):
    command = "SELECT username FROM Interpreter WHERE username LIKE %s;"
    database_cursor.execute(command, (username,))
    rows = database_cursor.fetchall()
    if(len(rows) == 0):
        print("I don't exist")
        return False
    else:
        print("I exist!")
        return True


def check_for_job_poster_username(database_cursor, username):
    command = "SELECT username FROM JobCreator WHERE username LIKE %s;"
    database_cursor.execute(command, (username,))
    rows = database_cursor.fetchall()
    if(len(rows) == 0):
        print("I don't exist")
        return False
    else:
        print("I exist!")
        return True


def check_for_interpreter_email(database_cursor, email):
    command = "SELECT email FROM Interpreter WHERE email LIKE %s;"
    database_cursor.execute(command, (email,))
    rows = database_cursor.fetchall()
    if(len(rows) == 0):
        print("I don't exist")
        return False
    else:
        print("I exist!")
        return True


def check_for_job_poster_email(database_cursor, email):
    command = "SELECT email FROM JobCreator WHERE email LIKE %s;"
    database_cursor.execute(command, (email,))
    rows = database_cursor.fetchall()
    if(len(rows) == 0):
        print("I don't exist")
        return False
    else:
        print("I exist!")
        return True


def check_for_interpreter_ID(database_cursor, ID):
    command = "SELECT InterpreterID FROM Interpreter WHERE InterpreterID = %s;"
    database_cursor.execute(command, (ID,))
    rows = database_cursor.fetchall()
    if (len(rows) == 0):
        print("I don't exist")
        return False
    else:
        print("I exist!")
        return True


def add_interpreter_account(database_cursor, first, middle, last, id, number, email, user, password):
    command = "INSERT INTO Interpreter (FirstName, MiddleName, LastName, InterpreterID, PhoneNumber, Email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    database_cursor.execute(command, (first, middle, last, id, number, email, user, password,))


def add_job_poster_account(database_cursor, first, middle, last, number, email, user, password):
    command = "INSERT INTO JobCreator (FirstName, MiddleName, LastName, PhoneNumber, Email, Username, Password) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    database_cursor.execute(command, (first, middle, last, number, email, user, password,))


##################################################
# Universal
##################################################
def try_login(database_cursor, email_username, password):
    command = "SELECT email, password FROM JobCreator WHERE email LIKE %s AND password LIKE %s;"
    database_cursor.execute(command, (email_username, password,))
    rows = database_cursor.fetchall()
    if(len(rows) == 1):
        print (" JOB CREATOR EMAIL")
        return [True, "email", 0]
    command = "SELECT username, password FROM JobCreator WHERE username LIKE %s AND password LIKE %s;"
    database_cursor.execute(command, (email_username, password,))
    rows = database_cursor.fetchall()
    if(len(rows) == 1):
        print ("JOB CREATOR USERNAME")
        return [True, "username", 0]
    command = "SELECT email, password FROM Interpreter WHERE email LIKE %s AND password LIKE %s;"
    database_cursor.execute(command, (email_username, password,))
    rows = database_cursor.fetchall()
    if (len(rows) == 1):
        print ("INTERPRETER EMAIL")
        return [True, "email", 1]
    command = "SELECT username, password FROM Interpreter WHERE username LIKE %s AND password LIKE %s;"
    database_cursor.execute(command, (email_username, password,))
    rows = database_cursor.fetchall()
    if (len(rows) == 1):
        print ("INTERPRETER USERNAME")
        return [True, "username", 1]
    else:
        return [False, "", -1]


def get_email_from_username(database_cursor, username):
    command = "SELECT email FROM JobCreator WHERE username LIKE %s;"
    database_cursor.execute(command, (username,))
    rows = database_cursor.fetchall()
    if(len(rows) == 1):
        return rows
    else:
        command = "SELECT email FROM Interpreter WHERE username LIKE %s;"
        database_cursor.execute(command, (username,))
        rows = database_cursor.fetchall()
        return rows


def create_job(database_cursor, street, street2, city, zip, LEP, claim, serivce, check, start, end, des, email):
    command = "INSERT INTO Address (LocationType, Street, Street2, City, State, County, Zipcode) " \
              "VALUES ('1', %s, %s, %s, 'WA', '033', %s);"
    database_cursor.execute(command, (street, street2, city, zip,))
    command = "SELECT ID FROM Address WHERE Street LIKE %s AND Zipcode = %s;"
    database_cursor.execute(command, (street, zip,))
    result = database_cursor.fetchall()

    command = "INSERT INTO Job (PostingTime, Address, LEPNumber, ClaimNumber, PayerID, Language, ServiceDate, CheckInTime, StartTime, EndTime, PriorityLevel, Description) " \
              "VALUES ('1999-01-08 04:05:06', %s, %s, %s, '1', 'es', %s, %s, %s, %s, '0', %s);"
    database_cursor.execute(command, (result[0], LEP, claim, serivce, check, start, end, des))


    command = "SELECT ID FROM Job WHERE Address = %s AND ServiceDate = %s AND StartTime = %s;"
    database_cursor.execute(command, (result[0], serivce, start))
    jobID = database_cursor.fetchall()
    print(jobID[0][0])

    command = "SELECT ID FROM JobCreator WHERE email LIKE %s;"
    database_cursor.execute(command, (email,))
    emailID = database_cursor.fetchall()
    print(emailID[0])

    command = "INSERT INTO PostedJobs (JobCreatorID, JobID) " \
              "VALUES (%s, %s);"
    database_cursor.execute(command, (emailID[0][0], jobID[0][0]))

    command = "INSERT INTO SavedLocations (JobCreatorID, AddressID) " \
              "VALUES (%s, %s);"
    database_cursor.execute(command, (emailID[0][0], result[0]))
