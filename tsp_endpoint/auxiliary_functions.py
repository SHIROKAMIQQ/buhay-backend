import networkx as nx
from osmnx.distance import great_circle
from tsp_endpoint.models import Point
from typing import List

async def create_graph(points: List[Point]) -> nx.Graph:
    
    n = len(points) 
    G = nx.Graph()

    # Add points[i] as the ith node of the graph
    for i in range(n):
        G.add_node(
            i, 
            location_name = points[i].location_name, 
            lat = points[i].coordinates[0], 
            lng = points[i].coordinates[1]
        )
    
    # Add edge(i,j) for each possible i,j combination such that its weight is the haversine distance between Point i and Point j
    for i in range(n):
        lat_i, lng_i = points[i].coordinates
        for j in range(i+1, n):
            lat_j, lng_j = points[j].coordinates
            G.add_edge(
                i, j,
                weight = great_circle(lat_i, lng_i, lat_j, lng_j)
            )
    
    return G