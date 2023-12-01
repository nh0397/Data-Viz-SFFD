# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash.dcc import Loading
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from appshell.data_loader import fig_call_type, fig_neighborhood, fig_response_time

graph_style = {
    "width": "75%",
    "height": "90%",
    "margin-left": "12vw",
    "display": "block",
}

heading_style = {"color": "rgb(255, 107, 107)", "text-align": "center", "margin-top": "20px"}

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2("User Empowerment", style=heading_style),
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label="Call Type",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Incident Counts by Call Type", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph11',
                                                    figure=fig_call_type,
                                                    style={**graph_style, "margin-top": "8vh"}
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Neighborhood District",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Incident Counts by Neighborhood District", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph12',
                                                    figure=fig_neighborhood,
                                                    style={**graph_style, "margin-top": "4vh"}
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Response Time",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Average Response Time by Neighborhood District", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph13',
                                                    figure=fig_response_time,
                                                    style={**graph_style, "margin-top": "4vh"}
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                    ]
                ),
            ],
            style={"width": "95%", "float": "left", "height": "100px", "padding": "20px"},
        ),
    ],
    style={"margin-top": "100px"},
)
