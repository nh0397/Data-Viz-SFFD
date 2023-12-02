# pages/home/homepage.py
from dash import html, dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.Img(src="../../../assets/SFFD.jpg", style={"width": "60%", "height": "80%", "margin-left": "18vw", "margin-top": "4vh", "display": "block", "border-radius": "8px"}),
                html.Div(
                    id="about-project",
                    style={"max-width": "800px", "margin": "20px auto", "padding": "20px", "border": "1px solid #ddd", "border-radius": "8px", "background-color": "#f7f7f7"},  # Adjusted padding after the border
                    children=[
                        html.H2("About the Project", style={"color": "rgb(255, 107, 107)"}),
                        dcc.Markdown(
                            """
                            A comprehensive analysis project leveraging the Fire Department Data Set to uncover
                            trends of three critical categories: Fire Calls-For-Service, Fire Incidents, and Fire 
                            Violations spanning multiple years. This project aims to provide valuable insights into 
                            the dynamics of fire-related incidents and safety compliance issues in our community. 
                            By tracking incident trends, identifying hotspots, and assessing compliance patterns over time, 
                            we can enhance public safety strategies, optimize resource allocation, and foster a safer 
                            environment for our city's residents. Through in-depth trend analysis and geospatial mapping, 
                            this project will contribute to a data-driven approach to improving the effectiveness of our 
                            local fire department and ensuring the well-being of our community.
                            """
                        ),
                    ],
                ),
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "padding": "20px"},  # Adjusted padding after the border
        ),
    ],
    style={"margin-top": "100px", "width": "100%", "height": "calc(100vh - 100px)"},
)
