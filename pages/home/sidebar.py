# sidebar.py

import dash_mantine_components as dmc
from dash import html, Output, Input, callback
from dash_iconify import DashIconify
from dash import dcc

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
            style={"background-color": "transparent", "border": "none", "color": "rgb(255, 107, 107)"},
        ),
        dmc.Drawer(
            title="Navigate through here",
            id="drawer-fancy",
            children=[
                html.Ul(
                    [
                        html.Li(
                            dcc.Link(
                                href="/",
                                children=[
                                    DashIconify(
                                        icon="bi:house-door",
                                        width=22,
                                        style={"margin-right": "8px"},
                                    ),
                                    "Home",
                                ],
                            ),
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page1",
                                children=[
                                    DashIconify(
                                        icon="bi:gear",
                                        width=22,
                                        style={"margin-right": "8px"},
                                    ),
                                    "Settings",
                                ],
                            ),
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page3",
                                children=[
                                    DashIconify(
                                        icon="bi:person",
                                        width=22,
                                        style={"margin-right": "8px"},
                                    ),
                                    "Profile",
                                ],
                            ),
                        ),
                        html.Li(
                            dcc.Link(
                                href="/page4",
                                children=[
                                    DashIconify(
                                        icon="bi:info-circle",
                                        width=22,
                                        style={"margin-right": "8px"},
                                    ),
                                    "About",
                                ],
                            ),
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
