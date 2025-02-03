import pytest
import warnings
import json

from typing import List

from fastapi import status
from httpx import ASGITransport, AsyncClient
from main import app, startup_event

from random import randint
import time

@pytest.mark.asyncio
async def test_tsp():
    start = time.time()
    async with startup_event(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            request = client.build_request(url="/tsp", method="GET", json=[
                {
                    "location_name": "0",
                    "coordinates": [1, 1]
                },
                {
                    "location_name": "1",
                    "coordinates": [10, 10]
                },
                {
                    "location_name": "2",
                    "coordinates": [2, 2]
                },
                {
                    "location_name": "3",
                    "coordinates": [0, 0]
                }
            ])
            response = await client.send(request)
        end = time.time()
        print("TIME TAKEN: ", end-start)
        assert response.json() == [
            {
                "location_name": "0",
                "coordinates": [
                    1.0,
                    1.0
                ]
            },
            {
                "location_name": "3",
                "coordinates": [
                    0.0,
                    0.0
                ]
            },
            {
                "location_name": "2",
                "coordinates": [
                    2.0,
                    2.0
                ]
            },
            {
                "location_name": "1",
                "coordinates": [
                    10.0,
                    10.0
                ]
            }
        ]

def generate_six_points(n):
    points: list[dict] = list()
    for i in range(n):
        lat = float(randint(0, 100_000))
        lng = float(randint(0, 100_000))
        p = {"location_name":f"{i}", "coordinates":[lat,lng]}
        points.append(p)
    return points

@pytest.mark.asyncio
async def test_time():
    test_cases = 10000
    n = 30
    total_start = time.time()
    for i in range(test_cases):
        body = generate_six_points(n)
        # print(body)
        start = time.time()
        async with startup_event(app):
            async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
                request = client.build_request(url="/tsp", method="GET", json=body)
                response = await client.send(request)
            end = time.time()
            # print(response.json())
            # print(f"RANDOM TEST {i+1} TIME TAKEN: ", end-start)
    total_end = time.time()
    print(f"TIME TAKEN FOR {test_cases} TEST CASES: ", total_end-total_start)
    print(f"AVERAGE TIME FOR {test_cases} TEST CASES: ", (total_end-total_start)/test_cases)