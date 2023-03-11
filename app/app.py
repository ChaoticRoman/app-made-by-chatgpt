import json
import os
from datetime import datetime as dt

import dash
from dash import dcc
from dash import html

import plotly.express as px

import pandas as pd

import requests

app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Real-time Scatter Plot"),
    dcc.Graph(id="scatter-plot"),
    dcc.Interval(
        id='interval-component',
        interval=1000, # in milliseconds
        n_intervals=0
    )
])


def title():
    return f"Data {dt.utcnow()} UTC"


@app.callback(
    dash.dependencies.Output("scatter-plot", "figure"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)
def update_graph(n):
    url = os.environ["DATA_API_URL"]
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame(data)
    fig = px.scatter(df, x="x", y="y", title=title())
    return fig


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
