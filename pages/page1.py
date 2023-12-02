# pages/page1.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash.dcc import Loading
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from appshell.data_loader import fig_column_chart, pie_visual_chart, fig_map

graph_style = {
    "width": "75%",
    "height": "90%",
    "margin-left": "12vw",
    "margin-top": "4vh",
    "display": "block",
}  # Adjusted styles for the graphs

# Define the layout for page1
layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2(
                    "Fire Incidents Analysis",
                    style={
                        "color": "rgb(255, 107, 107)",
                        "text-align": "center",
                        "margin-top": "20px",
                    },
                ),
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label="Column Chart",
                            children=[
                                html.H3("Count of Final Calls of Distress", style={"text-align": "center"}),
                                dcc.Graph(
                                    id="example-graph3",
                                    figure=fig_column_chart,
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
                            label="Pie Chart",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Types of Final Call Distress", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph7',
                                                    figure=pie_visual_chart,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Map",
                            children=[
                                html.H3("Different Call Types", style={"text-align": "center"}),
                                dcc.Graph(
                                    id="example-graph4",
                                    figure=fig_map,
                                    style={
                                        "width": "100%",
                                        "height": "100%",
                                        "margin-top": "20px",
                                        "display": "block",
                                    },
                                )
                            ],
                        )
                    ]
                ),
            ],
            style={
                "width": "80%",
                "float": "left",
                "height": "calc(100vh - 100px)",
                "padding": "20px",
            },
        ),
    ],
    style={"margin-top": "100px"},
)
