from dotenv import load_dotenv
import os 
import sys
import psycopg2

load_dotenv()

class Database:
    def __init__(self):
        self.conn = self.connect()

    def connect(self):
        """
        Connect to database and return connection
        """
        print("Connecting to PostgreSQL Database...")
        try:
            load_dotenv()
            conn = psycopg2.connect(
                    host = os.getenv("POSTGRES_HOST"),
                    dbname = os.getenv("POSTGRES_DB"),
                    user = os.getenv("POSTGRES_USER"),
                    password = os.getenv("POSTGRES_PASSWORD"),
                    port = os.getenv("POSTGRES_PORT")
                )
        except psycopg2.OperationalError as e:
            print(f"Could not connect to Database: {e}")
            sys.exit(1)

        return conn

