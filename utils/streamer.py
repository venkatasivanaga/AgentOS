import asyncio
import websockets
import json

async def broadcast_step(step_data: dict):
    """Pushes an agent execution step to the TypeScript WebSocket server."""
    try:
        # Connects to the Node.js middleware server
        async with websockets.connect("ws://localhost:8080") as websocket:
            await websocket.send(json.dumps(step_data))
    except ConnectionRefusedError:
        print("[!] Warning: WebSocket server not running. Skipping UI broadcast.")
    except Exception as e:
        print(f"[!] WebSocket Error: {e}")
