import psycopg2
import os

class Database:

    def login_user(self, email, password):
        print("LOGIN")
        print("EMAIL", email)
        print("PASSWORD", password)

    def register_user(self, username, email, password):
        print("REGISTER")
        print("Username", username)
        print("EMAIL", email)
        print("PASSWORD", password)


    #Mock up stuff down below

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