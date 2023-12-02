# sidebar.py

import dash_mantine_components as dmc
from dash import html, Output, Input, callback
from dash_iconify import DashIconify
from dash import dcc

# Define the common text color
text_color = "rgb(255, 107, 107)"

layout = html.Div(
    [
        dmc.Button(
            [
                DashIconify(
                    icon="ep:expand",
                    width=22,
                    style={"margin-right": "8px"},  # Add some right margin for spacing
                ),
                "",
            ],
            id="drawer-transition-button",
            style={"background-color": "transparent", "border": "none", "color": text_color},
        ),
        dmc.Drawer(
            title="Navigate through here",
            id="drawer-fancy",
            children=[
                html.Ul(
                    [
                        html.Li(
                            dcc.Link(
                                href="/page1",
                                children=[
                                    DashIconify(
                                        icon="bi:file-earmark-text",
                                        width=22,
                                        style={"margin-right": "8px", "color": text_color},
                                    ),
                                    "Primary Causes of Fire-related Calls-for-Service",
                                ],
                            ),
                            style={"margin-bottom": "10px"},  # Add margin-bottom for spacing
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page2",
                                children=[
                                    DashIconify(
                                        icon="bi:bar-chart-line",
                                        width=22,
                                        style={"margin-right": "8px", "color": text_color},
                                    ),
                                    "Patterns in Fire Incidents",
                                ],
                            ),
                            style={"margin-bottom": "10px"},  # Add margin-bottom for spacing
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page3",
                                children=[
                                    DashIconify(
                                        icon="bi:graph-up",
                                        width=22,
                                        style={"margin-right": "8px", "color": text_color},
                                    ),
                                    "Patterns and Trends in Historical Fire Data",
                                ],
                            ),
                            style={"margin-bottom": "10px"},  # Add margin-bottom for spacing
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page4",
                                children=[
                                    DashIconify(
                                        icon="bi:people",
                                        width=22,
                                        style={"margin-right": "8px", "color": text_color},
                                    ),
                                    "User Empowerment",
                                ],
                            ),
                            style={"margin-bottom": "10px"},  # Add margin-bottom for spacing
                        ),
                    ],
                    style={"list-style-type": "disc", "padding-left": "20px"},  # Use "disc" for bullet points
                ),
            ],
            padding="md",
            transition="rotate-left",
            transitionDuration=250,
            zIndex=10000,
            transitionTimingFunction="ease",
            style={"flexDirection": "column"},
        ),
    ],
)

@callback(
    Output("drawer-fancy", "opened"),
    Input("drawer-transition-button", "n_clicks"),
    prevent_initial_call=True,
)
def drawer_demo(n_clicks):
    return True
