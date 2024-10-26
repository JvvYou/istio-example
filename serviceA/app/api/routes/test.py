from fastapi import APIRouter, Request
import requests
from app.utils import getForwardHeaders

router = APIRouter()


@router.get("/")
async def root(request: Request):
    headers = getForwardHeaders(request)
    # response = requests.get('http://127.0.0.1:9000/api/v1/testB/', headers=headers)
    responseB = requests.get('http://service-b:9000/api/v1/testB/', headers=headers)

    responseC = requests.get('http://service-c:9000/api/v1/testC/', headers=headers)
    return f'{responseB.content} and {responseC.content}'


@router.get("/stc/")
async def sc(request: Request):
    headers = getForwardHeaders(request)
    # response = requests.get('http://127.0.0.1:9000/api/v1/testC/', headers=headers)
    response = requests.get('http://service-c:9000/api/v1/testC/', headers=headers)
    return response.content


@router.get("/get_headers/")
async def get_headers(request: Request):
    headers = request.headers
    return headers
