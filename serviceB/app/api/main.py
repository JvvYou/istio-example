from fastapi import APIRouter

from app.api.routes import testB, testC

api_router = APIRouter()
api_router.include_router(testB.router, prefix="/testB", tags=["testB"])
api_router.include_router(testC.router, prefix="/testC", tags=["testC"])
