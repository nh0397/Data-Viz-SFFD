# pages/home/homepage.py

from dash import html
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
import pandas as pd
from dash import dcc
import plotly.express as px
from appshell.data_loader import fig_timeseries

# Define the layout for page2
layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2("Patterns in Fire Incidents", style={"color": "rgb(255, 107, 107)", "text-align": "center", "margin-top": "20px"}),
                dcc.Graph(
                    id='example-graph6',
                    figure=fig_timeseries,
                    style={"width": "75%", "height": "90%", "margin-left": "12vw", "margin-top": "8vh", "display": "block"}
                ),
            ],
        ),
    ],
    style={"margin-top": "100px"},
)
