# TSP Endpoint

The _tsp endpoint_ accepts a GET Request at the `/tsp` path. This request contains a list of <b>n</b> `Point`s which follows the format below.
```python
[
    {
        "location_name" : str|None,
        "coordinates" : [lat: float, lng: float]
    }
]
```

The endpoint then returns a list of <b>n</b> `Point`s such that:
<br /> - The sequence of `Point`s is the shortest path that visits all of the given points from the input. 
<br /> - The weight of each edge from one point to another is the haversine distance between the two points.
<br /> - The returned path always starts with the first point from the input list.

### Dependencies 

The _tsp endpoint_ uses [FastAPI] for its implementation to receive GET Requests.

It uses the `Graph` data structure and `travelling_salesman_problem()` function from [NetworkX] to solve for the shortest path. Additionally, the `great_circle()` function from [OSMnx] was used to calculate the haversine distance between each point pair.

[FastAPI]: https://fastapi.tiangolo.com
[NetworkX]: https://networkx.org/documentation/stable/index.html
[OSMnx]: https://osmnx.readthedocs.io/en/stable/index.html

### Input Schema
The _tsp endpoint_'s input is validated using [Pydantic] with the schema below. By using Pydantic, the _tsp endpoint_ raises an `HTTP Exception` with the `422_Unprocessable_Entity` status code. 

[Pydantic]: docs.pydantic.dev
``` python
from pydantic import BaseModel

class Point(BaseModel):
    location_name: str | None
    coordinates: Tuple[float, float] #[lat: float, lng: float]
```