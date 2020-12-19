# All Required Imports
from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
import pandas
import urllib.request
import logging
import boto3
from botocore.exceptions import ClientError


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
# parse case_url and scrape relivent data off of it
def case_urls(str):
    # case url data for web to no name of document on S3 buckets to view
    case_url = str
    index = str[-19:-4].find('-')
    hearing_date = str[(len(str)-19):-4]
    hearing_date = hearing_date[index+1:]
    decision_date = hearing_date
    index = str.find('-')
    indexend = str.find(hearing_date)
    a = str[indexend-8:indexend-1].find('-') +1
    str[indexend-8+a:indexend-1]
    department=str[indexend-8+a:indexend-1]
    b = str.find(department)
    c=str[:b].find('-')+1
    urlforloop = str[c:indexend-9+a]
    l = []
    for i in range(7,len(urlforloop)):
        if str[i:i+1].find('-') == -1 and str[i+2:i+3].isnumeric():
            l.append(i)
    h= min(l) - 10
    case_id = urlforloop[h:]
    t = urlforloop.find(case_id)
    refugee = urlforloop[:t+1]
    return case_id, case_url,hearing_date,decision_date,department,refugee
# file uploaders
@router.post("/upload/pdf")
async def pdf(file: UploadFile = File(...)):
    if len(file.filename) >= 1:
        # add these varibles to table's scrapes all the data we need from initional upload
        case_id, case_url,hearing_date,decision_date,department,refugee = case_urls(file.filename)
        
        # Uploads File
        #upload = upload_file(file, bucket='hrf-asylum-dsa-documents', object_name=case_url)
    return {"filename": file.filename,
            "case_id" : case_id,
            "case_url" : case_url,
            "hearing_date" : hearing_date,
            "decision_date" : decision_date,
            "department": department,
            "refugee": refugee,
            "Test": "test_results"}

# deals with data from csv
def csv_data(df):
    return ""

@router.post("/upload/file")
async def not_pdf(file: UploadFile = File(...)):
            #if len(file.filename) >= 1:
    # add these varibles to table's
    #df = pd.read_csv(file)
    #varibles = csv_data(df)
    return {"filename": file.filename}