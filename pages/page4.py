# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash.dcc import Loading
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from appshell.data_loader import incident_by_call_type_chart, incident_by_neighborhood_chart, average_response_time_chart

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
                html.H2("Incident & Response Time Analysis", style=heading_style),
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
                                                    figure=incident_by_call_type_chart,
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
                                                    figure=incident_by_neighborhood_chart,
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
                                                    figure=average_response_time_chart,
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
