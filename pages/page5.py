# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from appshell.data_loader import fig_call_type as fig_call_type
from appshell.data_loader import fig_neighborhood as fig_neighborhood
from appshell.data_loader import fig_response_time as fig_response_time



layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2("User Empowerment", style={"color": "rgb(255, 107, 107)", "text-align": "center", "margin-top": "20px"}),
                # Add other components as needed
            ],
            style={"width": "95%", "float": "left", "height": "100px", "padding": "20px"},
        ),
        html.Div(
            [
                html.H3("Incident Counts by Call Type", style={"text-align": "center"}),
                dcc.Graph(
                    id='example-graph11',
                    figure=fig_call_type,
                    style={"width": "75%", "height": "90%", "margin-left": "12vw", "margin-top": "8vh", "display": "block"}
                ),
            ],
        ),
        html.Div(
            [
                html.H3("Incident Counts by Neighborhood District", style={"text-align": "center"}),
                dcc.Graph(
                    id='example-graph12',
                    figure=fig_neighborhood,
                    style={"width": "75%", "height": "90%", "margin-left": "12vw", "margin-top": "4vh", "display": "block"}
                ),
            ],
        ),
        html.Div(
            [
                html.H3("Average Response Time by Neighborhood District", style={"text-align": "center"}),
                dcc.Graph(
                    id='example-graph13',
                    figure=fig_response_time,
                    style={"width": "75%", "height": "90%", "margin-left": "12vw", "margin-top": "4vh", "display": "block"}
                ),
            ],
        )
    ],
    style={"margin-top": "100px"},
)