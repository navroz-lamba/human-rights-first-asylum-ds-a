"""This file has all the end points"""

from fastapi import APIRouter
# from app.schemas import 
#from app.database import session_local, engine
#from .database import session_local, engine
from .models import Case, User, Judge, BookMarkJudge, BookMarkCase

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
        name = con.engine.url.__repr__()
        return {'judge': name} 