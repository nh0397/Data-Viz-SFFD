# pages/home/homepage.py

from dash import html
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
import pandas as pd
from dash import dcc
import plotly.express as px

fire_incidents = pd.read_csv("C:/Users/sandh/OneDrive/Desktop/SFSU SEM 1/sem_proj_dataviz/Fire_Incidents.csv", low_memory = False)

# Convert the column to datetime if it's not already in datetime format
fire_incidents['Incident Date'] = pd.to_datetime(fire_incidents['Incident Date'])

# Group by date and count occurrences
df_grouped_2 = fire_incidents.groupby(fire_incidents['Incident Date'].dt.date).size().reset_index(name='Frequency')

# Create area chart
fig_timeseries = px.area(df_grouped_2, x='Incident Date', y='Frequency', labels={'Incident Date': 'Incident Date', 'Frequency': 'Number of Fire Incidents'}, title='Time Series Area Chart')




layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H1("Welcome to the page2", style={"color": "rgb(255, 107, 107)", "text-align": "center"}),
                # Add other components as needed
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "padding": "20px"},
        ),
        dcc.Graph(
            id='example-graph3',
            figure=fig_timeseries
        )
    ],
    style={"margin-top": "100px"},
)
