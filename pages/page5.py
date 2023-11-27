# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout


'''# Convert columns to datetime objects
fire_incidents['Alarm DtTm'] = pd.to_datetime(fire_incidents['Alarm DtTm'])
fire_incidents['Arrival DtTm'] = pd.to_datetime(fire_incidents['Arrival DtTm'])

# Calculate the time differences
fire_incidents['Time Difference'] = fire_incidents['Arrival DtTm'] - fire_incidents['Alarm DtTm']

# Calculate the mean time difference
mean_time_difference = fire_incidents['Time Difference'].mean()

print(f"Mean Time Difference between Alarm ringing and the Arrival of Fire Engine : {mean_time_difference}")'''

fire_department_calls_for_service = pd.read_csv('/Users/parthdesai/Downloads/Fire_Department_Calls_for_Service.csv', low_memory = False)

# Analyzing by Call Type Group to see which categories have the most incidents
call_type_counts = fire_department_calls_for_service['Call Type Group'].value_counts().reset_index()
call_type_counts.columns = ['Call Type Group', 'Count']

# Visualize the number of incidents by Call Type Group
fig_call_type = px.bar(call_type_counts, x='Call Type Group', y='Count', title='Incident Counts by Call Type Group')

# Analyzing by Neighborhoods to see where the most incidents occur
neighborhood_counts = fire_department_calls_for_service['Neighborhooods - Analysis Boundaries'].value_counts().reset_index()
neighborhood_counts.columns = ['Neighborhood', 'Count']

# Visualize the number of incidents by Neighborhood
fig_neighborhood = px.bar(neighborhood_counts, x='Neighborhood', y='Count', title='Incident Counts by Neighborhood')

# Response time analysis (difference between Received DtTm and On Scene DtTm)
fire_department_calls_for_service['Response Time'] = (fire_department_calls_for_service['On Scene DtTm'] - fire_department_calls_for_service['Received DtTm']).dt.total_seconds() / 60  # Convert to minutes
response_time_neighborhood = fire_department_calls_for_service.groupby('Neighborhooods - Analysis Boundaries')['Response Time'].mean().reset_index()

# Visualize the average response time by Neighborhood
fig_response_time = px.bar(response_time_neighborhood, x='Neighborhooods - Analysis Boundaries', y='Response Time', title='Average Response Time by Neighborhood')

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
        dcc.Graph(
            id='example-graph11',
            figure=fig_call_type
        ),
        dcc.Graph(
            id='example-graph12',
            figure=fig_neighborhood
        ),
        dcc.Graph(
            id='example-graph13',
            figure=fig_response_time
        )
    ],
    style={"margin-top": "100px"},
)
