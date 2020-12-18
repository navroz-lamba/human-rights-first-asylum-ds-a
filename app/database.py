"""This defines our database connection using SQLAlchemy."""
import os
from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import psycopg2
import boto3
import pandas
import sqlalchemy
routerdb = APIRouter()
load_dotenv()
POLICE_TABLE = """CREATE TABLE IF NOT EXISTS police_force (
    id SERIAL PRIMARY KEY NOT NULL,
    dates TIMESTAMP,
    added_on TIMESTAMP,
    links TEXT,
    case_id TEXT,
    city TEXT,
    state TEXT,
    lat FLOAT,
    long FLOAT,
    title TEXT,
    description TEXT,
    tags TEXT,
    verbalization INT,
    empty_hand_soft INT,
    empty_hand_hard INT,
    less_lethal_methods INT,
    lethal_force INT,
    uncategorized INT
);"""
#Connection to DB
name = os.getenv('name')
name = os.getenv('rds_username')
name = os.getenv('rds_password')
pg_conn = psycopg2.connect(dbname=name, user=rds_username, password=rds_password,host=rds_endpoint, port=port)
pg_curs = pg_conn.cursor()
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Base = declarative_base()
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
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# RDS_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
#                             'postgres', rds_password, rds_endpoint, port, database_name)

# # to connect to the database
# engine = create_engine(RDS_DATABASE_URL)
# # To be able to talk to the db, make a session 
# metadata = MetaData()
# metadata.bind = engine

# Base = declarative_base(metadata=metadata)
# Base.metadata.create_all(engine)
# to check the connection
# class Judge(Base):
#     __tablename__ = 'Judge'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     trump_appointed = Column(Boolean)
#     date_appointed = Column(String)
#     county = Column(String)
#     birth_date = Column(String)
#     biography = Column(String)
#     # judge can have multiple cases 
#     # on using backref it establishes .judge attribute on Case
#     cases = relationship("Case", backref='Judge') # Case.judge 


# class Case(Base):
#     __tablename__ = 'Case'

#     id = Column(String, primary_key=True)
#     case_id = Column(Integer)
#     case_url = Column(String)
#     court_type = Column(String)
#     hearing_type = Column(String)
#     credibility_of_refugee = Column(String)
#     refugee_origin = Column(String)
#     hearing_location = Column(String)
#     protected_ground = Column(String)
#     hearing_date = Column(String)
#     decision_date = Column(String)
#     social_group_type = Column(String)
#     # Using foreign key 
#     judge_id = Column(Integer, ForeignKey(Judge.id))


# class User(Base):
#     __tablename__ = 'user'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     email = Column(String)
#     avatarUrl = Column(String)
#     password = Column(String)
#     role = Column(String)


# class BookMarkJudge(Base):
#     __tablename__ = 'book_mark_judge'

#     id = Column(Integer, primary_key=True)
#     # using foreign key 
#     user_id = Column(Integer, ForeignKey(User.id))
#     # There could be multiple judges bookmarked
#     judges = relationship("Judge", backref='book_mark_judge') # Judge.book_mark_judge


# class BookMarkCase(Base):
#     __tablename__ = 'book_mark_case'

#     id = Column(Integer, primary_key=True)
#     # using foreign key 
#     user_id = Column(Integer, ForeignKey(User.id))
#     # There could be multiple cases bookmarked
#     cases = relationship("Case", backref='book_mark_case') # Case.book_mark_case

# base.metadata.create_all(db)

# if __name__ == "__main__":
#     print(engine)
#     print(Base)
#     print(RDS_DATABASE_URL)