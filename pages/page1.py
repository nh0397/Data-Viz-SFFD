# pages/home/homepage.py
import pandas as pd
import plotly.express as px
from dash import html
from dash import dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout

df_call_for_service = pd.read_csv("/Users/parthdesai/Downloads/SF_FD.csv")
# Extract latitude and longitude from the 'location' column
df_call_for_service['lat'], df_call_for_service['lon'] = zip(*df_call_for_service['Location'].str.strip('()').str.split(', ').apply(lambda x: (float(x[0]), float(x[1]))))
call_finaldisp_df = df_call_for_service.groupby('Call Final Disposition')['Location'].nunique()
call_type_df = df_call_for_service.groupby('Call Type')['Location'].nunique()

# Your data
data_finalcall = {
    'Final Call Distress': ['Administrative', 'Aircraft Emergency', 'Alarms', 'Assist Police', 'Citizen Assist / Service Call',
                  'Confined Space / Structure Collapse', 'Electrical Hazard', 'Elevator / Escalator Rescue', 'Explosion',
                  'Extrication / Entrapped (Machinery, Vehicle)', 'Fuel Spill', 'Gas Leak (Natural and LP Gases)', 'HazMat',
                  'High Angle Rescue', 'Industrial Accidents', 'Marine Fire', 'Medical Incident', 'Mutual Aid / Assist Outside Agency',
                  'Odor (Strange / Unknown)', 'Other', 'Outside Fire', 'Smoke Investigation (Outside)', 'Structure Fire',
                  'Suspicious Package', 'Traffic Collision', 'Train / Rail Incident', 'Transfer', 'Vehicle Fire', 'Water Rescue',
                  'Watercraft in Distress'],
    'Count': [56, 3, 4864, 31, 1704, 12, 525, 312, 107, 19, 185, 596, 75, 20, 41, 10, 18873, 1, 393, 1640, 1184, 287, 5279,
                 2, 3312, 10, 71, 501, 103, 24]
}

df1 = pd.DataFrame(data_finalcall)

# Provided data
data_calltype = {
    'Call Type': [
        'Administrative', 'Aircraft Emergency', 'Alarms', 'Assist Police', 'Citizen Assist / Service Call',
        'Confined Space / Structure Collapse', 'Electrical Hazard', 'Elevator / Escalator Rescue',
        'Explosion', 'Extrication / Entrapped (Machinery, Vehicle)', 'Fuel Spill',
        'Gas Leak (Natural and LP Gases)', 'HazMat', 'High Angle Rescue', 'Industrial Accidents',
        'Lightning Strike (Investigation)', 'Marine Fire', 'Medical Incident', 'Mutual Aid / Assist Outside Agency',
        'Odor (Strange / Unknown)', 'Oil Spill', 'Other', 'Outside Fire', 'Smoke Investigation (Outside)',
        'Structure Fire', 'Suspicious Package', 'Traffic Collision', 'Train / Rail Fire',
        'Train / Rail Incident', 'Transfer', 'Vehicle Fire', 'Water Rescue', 'Watercraft in Distress'
    ],
    'Count': [
        169, 8, 13572, 622, 15554, 48, 6563, 2245, 414, 97, 3068, 5295, 692, 53, 509, 3, 28, 32779,
        7, 3282, 372, 14491, 9005, 4269, 13659, 43, 9952, 1, 45, 2037, 4890, 233, 60
    ]
}

# Create DataFrame
df2 = pd.DataFrame(data_calltype)


# Column Chart
fig_column_chart = px.bar(df1, x='Final Call Distress', y='Count', title='Final Call Categorization Trend',
                           labels={'Count': 'Count', 'Final Call Distress': 'Final Call'},
                           color='Final Call Distress', height=600)
# Set background color for the column chart
fig_column_chart.update_layout(
    plot_bgcolor='lightblue',
    paper_bgcolor='lightblue'
)

# Line Chart
fig_line_chart = px.line(df2, x='Call Type', y='Count', title='Different Call Types',
                          labels={'Count': 'Count', 'Call Type': 'Call Type'},
                          line_shape='linear', height=600)
# Set background color for the line chart
fig_line_chart.update_layout(
    plot_bgcolor='lightgreen',
    paper_bgcolor='lightgreen'
)


# 3D Line Chart
fig_3d_bubble = px.scatter_3d(df2, x='Call Type', y='Count', z='Count',
                              color='Call Type', size='Count',
                              labels={'Count': 'Count', 'Call Type': 'Call Type'},
                              title='3D Bubble Chart of Call Types',
                              height=700)

# Set background color for the bubble chart
fig_3d_bubble.update_layout(
    plot_bgcolor='lightgray',
    paper_bgcolor='lightgray'
)

# df_call_for_service = pd.read_csv('/Users/parthdesai/Downloads/SF_FD.csv', low_memory = False)

# Convert date columns to datetime
date_columns = ['Received DtTm', 'Response DtTm', 'On Scene DtTm']
for col in date_columns:
    df_call_for_service[col] = pd.to_datetime(df_call_for_service[col])

# We need to split those into two separate columns for latitude and longitude
df_call_for_service['latitude'], df_call_for_service['longitude'] = zip(*df_call_for_service['Location'].str.strip('()').str.split(', ').apply(lambda x: (float(x[0]), float(x[1]))))

# Trend over years
df_call_for_service['year'] = df_call_for_service['Received DtTm'].dt.year
yearly_calls = df_call_for_service.groupby('year').size()

# Plotting yearly trend
fig_yearly_trend = px.line(x=yearly_calls.index, y=yearly_calls.values, labels={'x': 'Year', 'y': 'Number of Calls'})
fig_yearly_trend.update_layout(title='Yearly Calls Trend')

# Plotting a geographical scatter plot for the incidents
# Adjust mapbox style as needed
fig_map = px.scatter_mapbox(df_call_for_service, lat='latitude', lon='longitude', zoom=12, height=500,
                            color='Call Type', title='Calls by Location')
fig_map.update_layout(mapbox_style="open-street-map")

layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H1("Primary Causes of Fire-Related Calls-for-Service", style={"color": "rgb(255, 107, 107)", "text-align": "center"}),
                # Add other components as needed
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "padding": "20px"},
        ),
        dcc.Graph(
            id='example-graph1',
            figure=fig_line_chart
        ),
        dcc.Graph(
            id='example-graph2',
            figure=fig_3d_bubble
        ),
        dcc.Graph(
            id='example-graph3',
            figure=fig_column_chart
        ),
        dcc.Graph(
            id='example-graph4',
            figure=fig_map
        ),
        dcc.Graph(
            id='example-graph5',
            figure=fig_yearly_trend
        )
    ],
    style={"margin-top": "100px"}    
)
