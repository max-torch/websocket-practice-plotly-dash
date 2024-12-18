# websocket practice plotly dash
 
This is a demonstration of using websockets with plotly dash. The websocket server is written in python using the `websockets` library. The client is a plotly dash app that updates a graph in real time. The server sends data to the client every few milliseconds. The client receives the data and updates the graph. The graph is updated every few milliseconds. The server and client are running on the same machine. The server is running on port 8765 and the client is running on port 8050. The server and client communicate using the websocket protocol. The server sends data to the client using the websocket protocol. The client receives data from the server.

The data that the server is sending is coming from a USB microphone, and is the volume.

## How to run

1. Install dependencies using `pip install -r requirements.txt`.
2. Make sure your microphone is set as the audio input device of your operating system.
3. Start `websocket_server.py` using python.
4. Start `dash_websocket_client.py` using python.
5. Open the dash app in the browser using port 8050 of local host.
6. Talk into your microphone.
