"""This file has all the end points"""

from fastapi import APIRouter
# from app.schemas import 
#from app.database import session_local, engine
from app.models import Case, User, Judge, BookMarkJudge, BookMarkCase

router = APIRouter()


@router.get("/info")
async def update_data():
        return print("database works")