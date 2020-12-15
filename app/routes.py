"""This file has all the end points"""

from fastapi import APIRouter
# from app.schemas import 
from app.database import session_local, engine
from app.models import Case, User, Judge, BookMarkJudge, BookMarkCase

router = APIRouter()


@router.get("/info")
async def get_url():

    with engine.connect() as con:
        url_without_password = con.engine.url.__repr__()

        return {'url': url_without_password} 