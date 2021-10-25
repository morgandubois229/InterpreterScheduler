import psycopg2


def create_connection():
    scheduler_connection = psycopg2.connect(database="scheduler", user="postgres", password="cat123", host="127.0.0.1",
                                            port="5432")
    scheduler_connection.autocommit = True

    return scheduler_connection

def close_connection(current_connection):
    current_connection.close()
