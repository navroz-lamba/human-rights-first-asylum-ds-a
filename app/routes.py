"""This file has all the end points"""

from fastapi import APIRouter
# from app.schemas import 
#from app.database import session_local, engine
from app.database import session_local, engine
from app.models import Case, User, Judge, BookMarkJudge, BookMarkCase

router = APIRouter()


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
        url_without_password = con.engine.url.__repr__()

        return {'case': url_without_password} 

@router.get("/judge")
async def update_judge():
        return print("database works")
async def get_judge():

    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()

        return {'url': url_without_password} 

@router.get("/book_mark_judge")
async def update_bookmark_judge():
        return print("database works")
async def get_book_mark_judge():

    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()

        return {'user': url_without_password}

@router.get("/book_mark_case")
async def update_bookmark_case():
        return print("database works")
async def get_book_mark_case():

    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()

        return {'user': url_without_password} 