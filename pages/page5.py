# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from pages.load_data import df_call_for_service


'''# Convert columns to datetime objects
fire_incidents['Alarm DtTm'] = pd.to_datetime(fire_incidents['Alarm DtTm'])
fire_incidents['Arrival DtTm'] = pd.to_datetime(fire_incidents['Arrival DtTm'])

# Calculate the time differences
fire_incidents['Time Difference'] = fire_incidents['Arrival DtTm'] - fire_incidents['Alarm DtTm']

# Calculate the mean time difference
mean_time_difference = fire_incidents['Time Difference'].mean()

print(f"Mean Time Difference between Alarm ringing and the Arrival of Fire Engine : {mean_time_difference}")'''

# Analyzing by Call Type to see which categories have the most incidents
call_type_counts = df_call_for_service['Call Type'].value_counts().reset_index()
call_type_counts.columns = ['Call Type', 'Count']

# Visualize the number of incidents by Call Type
fig_call_type = px.bar(call_type_counts, x='Call Type', y='Count', title='Incident Counts by Call Type')

# Analyzing by Neighborhoods to see where the most incidents occur
neighborhood_counts = df_call_for_service['Neighborhood  District'].value_counts().reset_index()
neighborhood_counts.columns = ['Neighborhood  District', 'Count']

# Visualize the number of incidents by Neighborhood  District
fig_neighborhood = px.bar(neighborhood_counts, x='Neighborhood  District', y='Count', title='Incident Counts by Neighborhood  District')

# Convert 'Received DtTm' and 'On Scene DtTm' to datetime objects
df_call_for_service['Received DtTm'] = pd.to_datetime(df_call_for_service['Received DtTm'])
df_call_for_service['On Scene DtTm'] = pd.to_datetime(df_call_for_service['On Scene DtTm'])

# Calculate Response Time in minutes
df_call_for_service['Response Time'] = (df_call_for_service['On Scene DtTm'] - df_call_for_service['Received DtTm']).dt.total_seconds() / 60

# Group by neighborhood and calculate the mean response time
response_time_neighborhood = df_call_for_service.groupby('Neighborhood  District')['Response Time'].mean().reset_index()

# Visualize the average response time by Neighborhood  District using Plotly Express
fig_response_time = px.bar(response_time_neighborhood, x='Neighborhood  District', y='Response Time', title='Average Response Time by Neighborhood  District')
fig_response_time.update_layout(xaxis_title='Neighborhood  District', yaxis_title='Average Response Time (minutes)')

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
