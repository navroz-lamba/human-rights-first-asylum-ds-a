"""This file has all the end points"""

from fastapi import APIRouter, File, UploadFile
from app.models import Case, User, Judge, Base
from app import models
from sqlalchemy import *
from .database import Base, engine
from .models import Judge, Case

router = APIRouter()


@router.get("/info")
async def update_data():
        return print("route works")
async def get_url():
    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()
        return {'url': url_without_password} 


@router.get("/case")
async def update_case():
        return print("route works")
async def get_case():
    with engine.connect() as con:
        case_url = con.engine.url.__repr__()
        return {'case_url':case_url } 


@router.get("/judge")
async def update_judge():
        return print("route works")
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
