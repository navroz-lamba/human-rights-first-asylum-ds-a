# All Required Imports
from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
import pandas
import urllib.request
import logging
import boto3
from botocore.exceptions import ClientError
import response

# Connect POST request ot the api routor
router = APIRouter()

# deals with uploading file to S3 buckets
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return "didn't upload to S3"
    return "Uploaded :)"

# file uploaders
@router.post("/upload/pdf")
async def pdf(file: UploadFile = File(...)):
    if len(file.filename) >= 1:
        # parse case_url and scrape relivent data off of it
        def case_url(str):
            # case url data for web to no name of document on S3 buckets to view
            case_url = str[:-4]
            hearing_date = ""
            decision_date = ""
            department = ""
            refugee = ""
            return case_url,hearing_date,decision_date,department,refugee
        
        # add these varibles to table's scrapes all the data we need from initional upload
        case_url,hearing_date,decision_date,department,refugee = case_url(file.filename)
        
        # Uploads File
        upload = upload_file(file_name, bucket, object_name=None)
    return {"filename": file.filename,
            "case_url" : case_url,
            "dates" :  (hearing_date,decision_date),
            "department": department,
            "refugee": refugee,
            "Test": upload}

@router.post("/upload/file")
async def not_pdf(file: UploadFile = File(...)):
    # deals with data from csv
    df = pf.read_csv(file)
    def csv_data(df):
        return
    # add these varibles to table's
    varibles = csv_data(df)
    return {"filename": file.filename}