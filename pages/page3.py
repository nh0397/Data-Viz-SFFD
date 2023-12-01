# pages/home/page3.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash.dcc import Loading
from dash import callback, Output, Input
from pages.home.sidebar import layout as sidebar_layout
from appshell.data_loader import fig1, fig2, fig3, fig4

graph_style = {
    "width": "75%",
    "height": "90%",
    "margin-left": "12vw",
    "margin-top": "4vh",
    "display": "block",
}  # Adjusted styles for the graphs

heading_style = {"color": "rgb(255, 107, 107)", "text-align": "center", "margin-top": "20px"}

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H2("Patterns and Trends in Historical Fire Data", style=heading_style),
                dcc.Tabs(
                    [
                        dcc.Tab(
                            label="Graph 1",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Graph 1 Title", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph7',
                                                    figure=fig2,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Graph 2",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Graph 2 Title", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph8',
                                                    figure=fig3,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Graph 3",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Graph 3 Title", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph9',
                                                    figure=fig4,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Graph 4",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Graph 4 Title", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph10',
                                                    figure=fig1,
                                                    style={**graph_style}  # Apply the common style for spacing
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
            style={
                "width": "95%",
                "float": "left",
                "height": "100px",
                "padding": "20px",
            },
        ),
    ],
    style={"margin-top": "100px"},
)
