from fastapi import APIRouter, Request
from app.utils import getForwardHeaders


router = APIRouter()


@router.get("/")
async def root(request: Request):
    headers = getForwardHeaders(request)
    # print(headers)
    # print("i am service c, come from service a.")
    return {"message": "i am service c, come from service b or a."}
