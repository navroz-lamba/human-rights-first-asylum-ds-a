
from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile

router = APIRouter()

# file uploaders
@router.post("upload/pdf")
async def pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("upload/file")
async def not_pdf(file: UploadFile = File(...)):
    return {"filename": file.filename}