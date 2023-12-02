# appshell/appshell.py
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash import Output, Input, clientside_callback, html, dcc
from pages.home.homepage import layout as create_homepage_content
from pages.page1 import layout as page1_content
from pages.page2 import layout as page2_content
from pages.page3 import layout as page3_content
from pages.page4 import layout as page4_content
from dash.dependencies import State

def create_home_link(label: str, icon=None) -> dmc.Anchor:
    if icon:
        return dmc.Anchor(
            dmc.ThemeIcon(
                DashIconify(
                    icon=icon,
                    width=30,  # Adjust the width as needed
                ),
                variant="outline",
                radius=30,
                size=36,
                color="red",
            ),
            label,
            size="xl",
            href="/",
            underline=False,
        )
    else:
        return dmc.Anchor(
            label,
            size="xl",
            href="/",
            underline=False,
        )

def create_header_link(icon: str, href: str, size: int=22, color: str="red") -> dmc.Anchor:
    return dmc.Anchor(
        dmc.ThemeIcon(
            DashIconify(
                icon=icon,
                width=size,
            ),
            variant="outline",
            radius=30,
            size=36,
            color=color,
        ),
        href=href,
        target="_blank",
    )

def create_header() -> dmc.Header:
    return dmc.Header(
        height=100,
        fixed=True,
        px=25,
        children=[
            dmc.Stack(
                justify="between",
                style={"height":80},
                children=[
                    dmc.Grid(
                        children=[
                            dmc.Col(
                                span="auto",
                                style={"display": "flex", "alignItems": "center"},  # Center align the content vertically
                                children=[
                                    dmc.Image(
                                        src="../assets/Logo.png",
                                        alt="App Logo",
                                        height=50,
                                        width=50,
                                        radius="50%",
                                    ),
                                ],
                            ),
                            dmc.Col(
                                span="content",
                                pt=0,  # Set top padding to 0
                                style={"display": "flex", "alignItems": "center"},  # Center align the content vertically
                                children=[
                                    dmc.MediaQuery(
                                        html.H1("FlareGraph", style={"color": "rgb(255, 107, 107)"}),
                                        styles={"display": "none"},
                                        largerThan="lg",
                                    ),
                                    dmc.MediaQuery(
                                        html.H1("FlareGraph: Exploring Fire Department Statistics in San Francisco", style={"color": "rgb(255, 107, 107)","font-size":"2vw"}),
                                        styles={"display": "none"},
                                        smallerThan="lg",
                                    ),
                                ],
                            ),
                            dmc.Col(
                                span="auto",
                                style={"display": "flex", "alignItems": "center", "flex-direction": "row-reverse"},
                                children=dmc.Group(
                                    position="right",
                                    spacing="xl",
                                    children=[
                                        create_home_link("ic:baseline-home", icon="ic:baseline-home"),
                                        dmc.ActionIcon(
                                            DashIconify(
                                                icon="radix-icons:blending-mode", width=22
                                            ),
                                            variant="outline",
                                            radius=30,
                                            size=36,
                                            color="red",
                                            id="color-scheme-toggle",
                                        ),
                                    ]
                                ),
                            )
                        ],
                        style={"margin": "auto 0 auto 0"}
                    )
                ]
            )
        ]
    )

def create_appshell(app):
    return dmc.MantineProvider(
        theme={
            "fontFamily": "'Inter', sans-serif",
            "primaryColor": "red",
            "components": {
                "Button": {"styles": {"root": {"fontWeight": 400}}},
                "NotificationsProvider": {
                    "styles": {"root": {"color": "red"}},  # Adjust the color as needed
                },
                "Header": {
                    "styles": {"root": {"color": "red"}},  # Adjust the color as needed
                },
            },
        },
        inherit=True,
        children=[
            dcc.Store(id="theme-store", storage_type="local"),
            dcc.Location(id="url"),
            dmc.NotificationsProvider(
                [
                    create_header(),  # Pass the app object to create_header
                ]
            ),
            html.Div(id="page-content"),  # Placeholder for page content
        ],
        id="plotly-dash-multipage-app-provider",
        withGlobalStyles=True,
        withNormalizeCSS=True,
    )

def display_page(pathname):
    if pathname == "/page4":
        # Pass the dataset to the layout
        return page4_content
    elif pathname == "/page3":
        return page3_content
    elif pathname == "/page1":
        # Pass the dataset to the layout
        return page1_content
    elif pathname == "/page2":
        return page2_content
    else:
        # If the pathname doesn't match any known pages, display the homepage
        return create_homepage_content

clientside_callback(
    """ function(data) { return data } """,
    Output("plotly-dash-multipage-app-provider", "theme"),
    Input("theme-store", "data"),
)

clientside_callback(
    """function(n_clicks, data) {
        if (data) {
            if (n_clicks) {
                const scheme = data["colorScheme"] == "dark" ? "light" : "dark"
                return { colorScheme: scheme } 
            }
            return dash_clientside.no_update
        } else {
            return { colorScheme: "light" }
        }
    }""",
    Output("theme-store", "data"),
    Input("color-scheme-toggle", "n_clicks"),
    State("theme-store", "data"),
)
