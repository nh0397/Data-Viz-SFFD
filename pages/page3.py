# pages/home/page3.py
import pandas as pd
import plotly.express as px
from dash import html, dcc
from dash import callback, Output, Input
from dash.dcc import Loading
from pages.home.sidebar import layout as sidebar_layout
from appshell.data_loader import trace_plot, correlation_plot, violin_plot, fig_yearly_trend

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
                            label="Correlation Matrix",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Correlation Matrix Between Attributes", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph8',
                                                    figure=correlation_plot,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Violin Plot",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Closing date by status", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph9',
                                                    figure=violin_plot,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Time Series",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Time Difference between Alarm and Arrival", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id='example-graph10',
                                                    figure=trace_plot,
                                                    style={**graph_style}  # Apply the common style for spacing
                                                ),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                        ),
                        dcc.Tab(
                            label="Yearly Trend",
                            children=[
                                Loading(
                                    type="circle",
                                    children=[
                                        html.Div(
                                            [
                                                html.H3("Trend of calls per year", style={"text-align": "center"}),
                                                dcc.Graph(
                                                    id="example-graph5",
                                                    figure=fig_yearly_trend,
                                                    style={**graph_style}
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
