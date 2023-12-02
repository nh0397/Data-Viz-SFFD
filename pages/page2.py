# pages/home/homepage.py

from dash import html
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
import pandas as pd
from dash import dcc
import plotly.express as px
from appshell.data_loader import fig_line_chart, fig_area_chart, fig_3d_bubble

# Define the layout for page2
layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2(
                    "Annual trend analysis of incidents considering their neighbourhoods",
                    style={
                        "color": "rgb(255, 107, 107)",
                        "text-align": "center",
                        "margin-top": "20px"
                    }
                ),
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label="Line Chart",
                            children=[
                                html.H3("Count of Different Types of Fire Incidents", style={"text-align": "center"}),
                                dcc.Graph(
                                    id="example-graph1",
                                    figure=fig_line_chart,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Area Chart",
                            children=[
                                html.H3("Count of Fire Incidents according to Date", style={"text-align": "center"}),
                                dcc.Graph(
                                    id="example-graph6",
                                    figure=fig_area_chart,
                                    style={
                                        "width": "75%",
                                        "height": "90%",
                                        "margin-left": "12vw",
                                        "margin-top": "8vh",
                                        "display": "block"
                                    }
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="3D Bubble Chart",
                            children=[
                                html.H3("Count of Fire Incidents according to Call Type", style={"text-align": "center"}),
                                dcc.Graph(
                                    id="example-graph2",
                                    figure=fig_3d_bubble,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        ),
                    ],
                ),
            ],
            style={
                "width": "80%",
                "float": "left",
                "height": "calc(100vh - 100px)",
                "padding": "20px",
            },
        )
    ],
    style={"margin-top": "100px"}
)
