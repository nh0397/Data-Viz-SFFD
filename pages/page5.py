# pages/home/homepage.py

from dash import html
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout


'''# Convert columns to datetime objects
fire_incidents['Alarm DtTm'] = pd.to_datetime(fire_incidents['Alarm DtTm'])
fire_incidents['Arrival DtTm'] = pd.to_datetime(fire_incidents['Arrival DtTm'])

# Calculate the time differences
fire_incidents['Time Difference'] = fire_incidents['Arrival DtTm'] - fire_incidents['Alarm DtTm']

# Calculate the mean time difference
mean_time_difference = fire_incidents['Time Difference'].mean()

print(f"Mean Time Difference between Alarm ringing and the Arrival of Fire Engine : {mean_time_difference}")'''



layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H1("Welcome to the page5", style={"color": "rgb(255, 107, 107)", "text-align": "center"}),
                # Add other components as needed
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "padding": "20px"},
        ),
    ],
    style={"margin-top": "100px"},
)
