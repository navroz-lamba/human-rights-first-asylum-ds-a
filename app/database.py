"""This defines our database connection using SQLAlchemy."""
import os
from fastapi import APIRouter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import psycopg2
import boto3
import pandas

# to load the credentials from .env file
load_dotenv()
rds_username = os.getenv('rds_username')
rds_password = os.getenv('rds_password')
rds_endpoint = os.getenv('rds_endpoint')
port = '5432'
database_name = 'postgres'

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
RDS_DATABASE_URL = 'postgresql://{}:{}@{}:{}/postgres'.format(
                            rds_username, rds_password, rds_endpoint, port, database_name)

# to connect to the database
engine = create_engine(RDS_DATABASE_URL)

# To be able to talk to the db, make a session 
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

Base = declarative_base()

# For S3 buckets database 
# access_key = os.getenv('access_key')
# secret_access_key = os.getenv('secret_access_key')


# S3 = boto3.client('s3',
#                         aws_access_key_id = access_key,
#                         aws_secret_access_key = secret_access_key)
                        
# # uploads pdf files added to dir
# for file in os.listdir():
#     if '.pdf' in file:
#         upload_file_bucket = "human-rights-first-asylum-analysis-documents"
#         upload_file_key = 'pdf/' + str(file)
#         S3.upload_file(file, upload_file_bucket, upload_file_key)
# to check the connection 
if __name__ == "__main__":
    print(engine)
    print(Base)