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
import fastapi-sqlalchemy
routerdb = APIRouter()
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
async def get_db() -> sqlalchemy.engine.base.Connection:
    """Get a SQLAlchemy database connection.
    
    Uses this environment variable if it exists:  
    DATABASE_URL=dialect://user:password@host/dbname
    Otherwise uses a SQLite database for initial local development.
    """
    load_dotenv()
    rds_username = str(os.getenv('rds_username'))
    rds_password = str(os.getenv('rds_password'))
    rds_endpoint = str(os.getenv('rds_endpoint'))
    port = '5432'
    database_name = 'postgres'
    #SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    SQLALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(rds_username, rds_password, rds_endpoint, port, database_name)
    engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)
    connection = engine.connect()
    try:
        yield connection
    finally:
        connection.close()


@routerdb.get('/info')
async def get_url(connection=Depends(get_db)):
    """Verify we can connect to the database, 
    and return the database URL in this format:
    dialect://user:password@host/dbname
    The password will be hidden with ***
    """
    url_without_password = repr(connection.engine.url)
    return {'database_url': url_without_password}
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