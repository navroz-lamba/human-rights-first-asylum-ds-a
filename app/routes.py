"""This file has all the end points"""

from fastapi import APIRouter, File, UploadFile
from app.database import session_local, engine
from app.models import Case, User, Judge

router = APIRouter()

# database Get request
@router.get("/info")
async def update_data():
        return print("database works")
async def get_url():
    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()
        return {'url': url_without_password} 

@router.get("/case")
async def update_case():
        return print("database works")
async def get_case():
    with engine.connect() as con:
        case_without_password = con.engine.case.__repr__()
        return {'case': case_without_password} 

@router.get("/judge")
async def update_judge():
        return print("database works")
async def get_judge():
    with engine.connect() as con:
        judge_without_password = con.engine.judge.__repr__()
        return {'judge': judge_without_password} 

# file uploaders database post request
@router.post("/upload/pdf")
async def pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("/upload/file")
async def not_pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}