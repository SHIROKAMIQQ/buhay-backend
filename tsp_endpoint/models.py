from pydantic import BaseModel
from typing import Tuple

class Point(BaseModel):
    location_name: str | None
    coordinates: Tuple[float, float]

    