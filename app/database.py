"""This defines our database connection using SQLAlchemy."""

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import psycopg2

# to load the credentials from .env file
load_dotenv()

rds_username = os.getenv('rds_username')
rds_password = os.getenv('rds_password')
rds_endpoint = 'asylumdb.cxip2v9lysxm.us-east-2.rds.amazonaws.com'
port = '5432'

class Engine:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(database="postgres",
                                                user=rds_username,
                                                password=rds_password,
                                                host=rds_endpoint,
                                                port=port)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            print("Cannot connect to Database")
    def create_table(self):
        create_table_command = "CREATE TABLE placeholder(id serial PRIMARY KEY, name varchar(100), age integer NOT NULL)"
        self.cursor.execute(create_table_command)


# to check the connection 
if __name__ == "__main__":
    base = Engine()

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
RDS_DATABASE_URL = 'postgresql://{}:{}@{}:{}'.format(
                            rds_username, rds_password, rds_endpoint, port)

# to connect to the database
engine = create_engine(RDS_DATABASE_URL)

# To be able to talk to the db, make a session 
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

Base = declarative_base()

# to check the connection 
if __name__ == "__main__":
    print(engine)
