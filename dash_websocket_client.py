from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash_extensions import WebSocket
import plotly.graph_objs as go
import collections

# Dash App Setup
app = Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id="live-graph"),
    WebSocket(id="ws", url="ws://localhost:8765"),
])

# Initialize a deque to store volume data
volume_data = collections.deque(maxlen=100)  # Store the last 100 data points

@app.callback(
    Output("live-graph", "figure"),
    Input("ws", "message")
)
def update_graph(message):
    if message and "data" in message and message["data"] is not None:
        volume = float(message["data"])
    else:
        volume = 0.0  # Default value or handle the error as needed

    # Append new volume data to the deque
    volume_data.append(volume)

    # Create a time series plot
    figure = {
        "data": [go.Scatter(x=list(range(len(volume_data))), y=list(volume_data), mode='lines+markers')],
        "layout": {
            "title": "Real-Time Volume",
            "xaxis": {"title": "Time"},
            "yaxis": {"title": "Volume", "range": [0, 50]},
        }
    }
    return figure

if __name__ == "__main__":
    app.run_server(debug=True)