"""This file has all the end points"""

from fastapi import APIRouter, File, UploadFile
from app.models import Case, User, Judge, Base
from app import models
from sqlalchemy import *
#from .database import Base, MetaData, engine
from .models import Judge, Case
router = APIRouter()
from app.database import Base

@router.get("/case")
async def update_case():
        return print("database works")
async def get_case():
    with Base.connect() as con:
        case_without_password = con.engine.case.__repr__()
        return {'case': case_without_password} 

@router.get("/judge")
async def update_judge():
        return print("database works")
async def get_judge():
    with Base.connect() as con:
        judge_without_password = con.engine.judge.__repr__()
        return {'judge': judge_without_password} 

# file uploaders database post request
@router.post("/upload/pdf")
async def pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("/upload/file")
async def not_pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}