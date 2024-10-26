from fastapi import APIRouter, Request
from app.utils import getForwardHeaders
import requests


router = APIRouter()


@router.get("/")
async def root(request: Request):
    headers = getForwardHeaders(request)
    responseC = requests.get('http://service-c:9000/api/v1/testC/', headers=headers)
    return responseC.content
    # return {"message": "i am service b, come from service a, v2"}


@router.get("/ddd")
async def testt():
    print("i am service b, not from service a, v2")
    return {"message": "i am service b, not from service a, v2"}
