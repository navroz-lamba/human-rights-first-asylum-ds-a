"""This defines our database connection using SQLAlchemy."""

import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import psycopg2
import boto3
# s3 bucket creation
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket='hrf-asylum-dsa-documents')

# # to load the credentials from .env file
# load_dotenv()

# rds_username = os.getenv('rds_username')
# rds_password = os.getenv('rds_password')
# rds_endpoint = 'asylumdb.cxip2v9lysxm.us-east-2.rds.amazonaws.com'
# port = '5432'
# database_name = 'hrfasyluma'

# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# RDS_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(rds_username, rds_password, rds_endpoint, port, database_name)

# # to connect to the database
# engine = create_engine(RDS_DATABASE_URL)

# # To be able to talk to the db, make a session 
# session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

Base = declarative_base()

# to check the connection 
if __name__ == "__main__":
    print(engine)
    print(Base)
