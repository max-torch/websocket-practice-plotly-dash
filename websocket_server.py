#!/usr/bin/env python

import asyncio
import websockets
import sounddevice as sd
import numpy as np

async def volume_stream(websocket):
    """Send real-time volume data to the connected client."""
    async def stream_volume():
        """Continuously stream microphone volume."""
        def get_volume(indata, frames, time, status):
            nonlocal volume
            volume = np.linalg.norm(indata) * 10

        volume = 0.0
        stream = sd.InputStream(callback=get_volume)
        with stream:
            stream.start()
            while True:
                # Send the current volume to the client
                await websocket.send(f"{volume:.2f}")
                await asyncio.sleep(0.02)  # Send updates every 20ms

    try:
        await stream_volume()
    except websockets.ConnectionClosed:
        print("Client disconnected.")

async def main():
    """Start the WebSocket server."""
    async with websockets.serve(volume_stream, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
