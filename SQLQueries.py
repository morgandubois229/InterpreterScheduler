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