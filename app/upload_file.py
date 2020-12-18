
from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile
import pandas
import urllib.request
router = APIRouter()

# deals with data from csv

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
        # add these varibles to table's
        case_url,hearing_date,decision_date,department,refugee = case_url(file.filename)
    return {"filename": file.filename,
            "case_url" : case_url,
            "dates" :  (hearing_date,decision_date),
            "department": department,
            "refugee": refugee}

@router.post("/upload/file")
async def not_pdf(file: UploadFile = File(...)):
    # deals with data from csv
    df = pf.read_csv(file)
    def csv_data(df):
        return
    # add these varibles to table's
    varibles = csv_data(df)
    return {"filename": file.filename}