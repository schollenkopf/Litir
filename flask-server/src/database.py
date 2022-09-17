import psycopg2
import os
import time

class EmailAlreadyExsists(Exception):
    """The email is already present in the DB"""
    pass

class WrongPassword(Exception):
    """The password is wrong"""
    pass

class Database:

    user_table = "users"
    n_users = 0
    logged_in_user = None

    def __init__(self) -> None:
        self.initTrue = self.init_tables()

    def init_tables(self):
        exit = False
        while(not exit):
            try:
                time.sleep(3)
                conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                            user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                            database=os.environ['POSTGRES_DATABASE']
                            )
                cursor = conn.cursor()
                cursor.execute(f"CREATE TABLE {self.user_table} (   id BIGSERIAL PRIMARY KEY NOT NULL,  "
                                                                "   username VARCHAR(200) NOT NULL,     "
                                                                "   email VARCHAR(200) NOT NULL,        "
                                                                "   password VARCHAR(200) NOT NULL,     "
                                                                "   UNIQUE (email)                      "
                                                                ")")
                conn.commit()
                conn.close()
                cursor.close()
                exit = True
            except:
                time.sleep(1)
        return True


    def login_user(self, email, password):
        if self.password_correct(email, password):
            self.logged_in_user = email
        elif self.email_already_exists(email):
            raise WrongPassword
        else:
            raise EmailAlreadyExsists

    def register_user(self, username, email, password):
        print("IS DATABASE UP", self.initTrue)
        if not self.email_already_exists(email):
            self.add_user(username, email, password)
            self.n_users += 1
            print("USER ADDED, NOW THE NUMBER OF USERS IS", self.n_users)
        else:
            raise EmailAlreadyExsists

    def email_already_exists(self, email):
        exists = False
        conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                     user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                     database=os.environ['POSTGRES_DATABASE']
                     )
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.user_table} WHERE email = '{email}'")
        response = cur.fetchall()
        print("LIST OF ELEMENTS WITH SAME EMAIL", response)
        if len(response) > 0:
            exists = True
        conn.close()
        cur.close()
        return exists

    #Mock up stuff down below

    def add_user(self, username, email, password):
        conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                     user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                     database=os.environ['POSTGRES_DATABASE']
                     )
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {self.user_table} (id, username, email, password) VALUES( {self.n_users}, '{username}', '{email}', '{password}')")
        conn.commit()
        conn.close()
        cursor.close()

    tableName = "words"

    def populate(self):
        conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                     user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                     database=os.environ['POSTGRES_DATABASE']
                     )
        cursor = conn.cursor()
        cursor.execute(f"CREATE TABLE {self.tableName} (part_id SERIAL PRIMARY KEY, italian VARCHAR(255), german VARCHAR(255))")
        cursor.execute(f"INSERT INTO {self.tableName} (part_id, italian, german) VALUES( 10, 'Ciao', 'Hallo')")
        conn.commit()
        conn.close()
        cursor.close()

    def fetch(self):
        conn = psycopg2.connect(host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                     user=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                     database=os.environ['POSTGRES_DATABASE']
                     )
        # Open a cursor to perform database operations
        cur = conn.cursor()

        # Execute a query
        cur.execute(f"SELECT * FROM {self.tableName}")

        # Retrieve query results
        records = cur.fetchall()
        conn.close()
        cur.close()
        return records