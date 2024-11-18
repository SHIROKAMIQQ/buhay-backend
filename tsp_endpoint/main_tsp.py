from fastapi import APIRouter
from fastapi.params import Body

from tsp_endpoint.models import Point
from tsp_endpoint.auxiliary_functions import create_graph
import networkx as nx
from typing import List

router = APIRouter()

@router.get("/tsp")
async def tsp(points: List[Point]) -> List[Point]:
    
    # Convert input points into a complete, weighted, undirected graph, in which the weights of the edges are the haversine distance between the adjacent vertices.
    G: nx.Graph = await create_graph(points)
    
    return points #THIS IS A FILLER