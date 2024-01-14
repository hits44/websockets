
import asyncio
# from websockets.sync.client import connect
from websockets.sync.client import connect

res= []
def hello():
    with connect("ws://localhost:8765") as websocket:
        websocket.send("Hello world!")
        message = websocket.recv()
        res.append(message)
        websocket.send("Hello world2!")
        message = websocket.recv()
        res.append(message)
        websocket.send("Hello world3!")
        message = websocket.recv()
        res.append(message)
        print(f"Received: {res}")

hello()