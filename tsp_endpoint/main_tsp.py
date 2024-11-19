from fastapi import APIRouter
from fastapi.params import Body

from tsp_endpoint.models import Point
from tsp_endpoint.auxiliary_functions import create_graph, node_to_json_parser
import networkx as nx
from typing import List

router = APIRouter()

@router.get("/tsp")
async def tsp(points: List[Point]) -> List[Point]:
    
    # Convert input points into a complete, weighted, undirected graph, in which the weights of the edges are the haversine distance between the adjacent vertices.
    G: nx.Graph = await create_graph(points)

    # Find the shortest route to visit all points  
    tsp_route = nx.approximation.traveling_salesman_problem(
        G = G,
        nodes = G.nodes,
        weight = "weight",
        cycle = False
    )
    return await node_to_json_parser(G, tsp_route)