from fastapi import APIRouter
from fastapi.params import Body

from tsp_endpoint.models import Point
from typing import List

router = APIRouter()

@router.get("/tsp")
async def tsp(points: List[Point]):
    return {"message": "BIG FILES"} #THIS IS A FILLER
