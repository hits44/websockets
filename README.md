# websockets in python

Why and whats the use?

used in doing real time apps , chat , calls,
where a connection is open and you can do the transaction

# server (uses asyncio for it's operation)

```python
#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
```

now what the websocket server is up , so whats next

next is the user or the client

```python
#!/usr/bin/env python

import asyncio
from websockets.server import serve

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
```
