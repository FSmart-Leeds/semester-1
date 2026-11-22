"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"
response = httpx.get(url)   # httpx object, get() method, returns a response object

if str(response) == "<Response [200 OK]>":
    print(response.json())      # response object, json() method
