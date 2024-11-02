from fastapi import APIRouter, HTTPException
from  fastapi.responses import JSONResponse

from app_lifecode.db.db import create_database

db_router = APIRouter(prefix="/api",tags=['api'])

@db_router.get("/create_table")
async def create_table():
    try:
        await create_database()
    except Exception as e:
        print(e)
        raise HTTPException(500, "Server error!")
    return JSONResponse({"message": "Models created!"}, status_code=201)

