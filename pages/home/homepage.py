# pages/home/homepage.py

from dash import html
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.Img(src="../../../assets/SFFD.jpg", style={"width": "70%", "height": "90%", "margin-left": "12vw","margin-top":"4vh", "display": "block"}),
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "overflow": "hidden"},
        ),
    ],
    style={"margin-top": "100px", "overflow": "hidden", "width": "100%", "height": "calc(100vh - 100px)"},
)
