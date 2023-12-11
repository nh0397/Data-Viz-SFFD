# appshell/data_loader.py
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

class DataHandler:
    def __init__(self):
        self.df_call_for_service = pd.DataFrame()
        self.fire_incidents = pd.DataFrame()
        self.fire_violations = pd.DataFrame()

    def load_data(self):
        """Load data only if not already loaded."""
        if self.df_call_for_service.empty:
            try:
                self.df_call_for_service = pd.read_pickle('./Data/df_call_for_service.pkl')
                self.df_call_for_service_sample = self.df_call_for_service.sample(1000)
            except FileNotFoundError:
                print("Warning: df_call_for_service.pkl not found.")
        if self.fire_incidents.empty:
            try:
                self.fire_incidents = pd.read_pickle('./Data/fire_incidents.pkl')
            except FileNotFoundError:
                print("Warning: fire_incidents.pkl not found.")
        if self.fire_violations.empty:
            try:
                self.fire_violations = pd.read_pickle('./Data/fire_violations.pkl')
            except FileNotFoundError:
                print("Warning: fire_violations.pkl not found.")

# Usage
data_handler = DataHandler()
data_handler.load_data()

# Access dataframes safely
df_call_for_service = data_handler.df_call_for_service
fire_incidents = data_handler.fire_incidents
fire_violations = data_handler.fire_violations
df_call_for_service_sample = data_handler.df_call_for_service_sample

# Convert date columns to datetime
date_columns = ['Received DtTm', 'Response DtTm', 'On Scene DtTm']
for col in date_columns:
    df_call_for_service[col] = pd.to_datetime(df_call_for_service[col])
    df_call_for_service_sample[col] = pd.to_datetime(df_call_for_service_sample[col])

# Convert the column to datetime if it's not already in datetime format
fire_incidents['Incident Date'] = pd.to_datetime(fire_incidents['Incident Date'])

# We need to split those into two separate columns for latitude and longitude
df_call_for_service['latitude'], df_call_for_service['longitude'] = zip(*df_call_for_service['Location'].str.strip('()').str.split(', ').apply(lambda x: (float(x[0]), float(x[1]))))
df_call_for_service_sample['latitude'], df_call_for_service_sample['longitude'] = zip(*df_call_for_service_sample['Location'].str.strip('()').str.split(', ').apply(lambda x: (float(x[0]), float(x[1]))))

# # Group by district and calculate the total count of violation codes
# district_counts = fire_violations.groupby('neighborhood district')['violation item'].count().reset_index(name='count')

# # Sort districts based on the total count in descending order
# district_counts_sorted = district_counts.sort_values(by='count', ascending=False)

# # Display the top three districts
# top_three_districts = district_counts_sorted.head(3)
# #have to print the top three districts with most number of violation codes.
# ttd = pd.DataFrame(top_three_districts)


# # Extract latitude and longitude from the 'location' column
# df_call_for_service['lat'], df_call_for_service['lon'] = zip(*df_call_for_service['Location'].str.strip('()').str.split(', ').apply(lambda x: (float(x[0]), float(x[1]))))
# call_finaldisp_df = df_call_for_service.groupby('Call Final Disposition')['Location'].nunique()
# call_type_df = df_call_for_service.groupby('Call Type')['Location'].nunique()

############################################################### PAGE 1 ###############################################################

######################## TAB 1 - LINE CHART ########################

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
data_calltype = pd.DataFrame(data_calltype)

# Create a beautiful line chart
fig_line_chart = px.line(data_calltype, x='Call Type', y='Count', 
                         labels={'Count': 'Count', 'Call Type': 'Call Type'},
                         line_shape='linear', height=600)

# Set background color for the line chart
fig_line_chart.update_layout(
    margin=dict(l=20, r=20, t=80, b=20),
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",
)

# Update x-axis tick angle for better readability
fig_line_chart.update_xaxes(tickangle=45)


######################## TAB 2 - 3D BUBBLE CHART ########################

# Create a visually appealing 3D Bubble Chart
fig_3d_bubble = px.scatter_3d(data_calltype, x='Call Type', y='Count', z='Count', color='Call Type', size='Count', labels={'Count': 'Count', 'Call Type': 'Call Type'}, height=700)

# Update layout for the 3D Bubble Chart
fig_3d_bubble.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color="#777",
    margin=dict(l=20, r=20, t=80, b=20),
    scene=dict(
        xaxis=dict(gridcolor='lightgray'),
        yaxis=dict(gridcolor='lightgray'),
        zaxis=dict(gridcolor='lightgray'),
    ),
    showlegend=False,
    xaxis_tickangle=45,  # Update x-axis tick angle for better readability
)


######################## TAB 3 - COLUMN CHART ########################

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

# Create a column chart
fig_column_chart = px.bar(data_finalcall, x='Final Call Distress', y='Count', 
                          labels={'Count': 'Count', 'Final Call Distress': 'Final Call'}, 
                          color='Final Call Distress', height=600)

# Set background color for the column chart
fig_column_chart.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",
)

######################## TAB 4 - SCATTER MAPBOX ########################

def create_scatter_mapbox(data, lat, lon, zoom, height, color):
    """
    Create a scatter mapbox plot.
    Sample data if it's too large to improve performance.
    """
    return px.scatter_mapbox(data, lat=lat, lon=lon, zoom=zoom, color=color, height=height, mapbox_style="open-street-map")

# Plotting a geographical scatter plot for the incidents
fig_map = create_scatter_mapbox(df_call_for_service_sample, lat='latitude', lon='longitude', zoom=12, height=500, color='Call Type')
fig_map.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",
)

######################## TAB 5 - YEARLY TREND LINE CHART ########################

# Trend over years
df_call_for_service['year'] = df_call_for_service['Received DtTm'].dt.year
yearly_calls = df_call_for_service.groupby('year').size()

fig_yearly_trend = px.line(x=yearly_calls.index, y=yearly_calls.values, labels={'x': 'Year', 'y': 'Number of Calls'})
fig_yearly_trend.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",
)
############################################################### PAGE 2 ###############################################################

######################## TAB 1 - TIME SERIES AREA CHART ########################

# Group by date and count occurrences
df_grouped_2 = fire_incidents.groupby(fire_incidents['Incident Date'].dt.date).size().reset_index(name='Frequency')

# Create area chart
fig_area_chart = px.area(df_grouped_2, x='Incident Date', y='Frequency', labels={'Incident Date': 'Incident Date', 'Frequency': 'Number of Fire Incidents'})
fig_area_chart.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",
)

############################################################### PAGE 3 ###############################################################

######################## TAB 1 - PIE CHART ########################

df1_sorted = df1.sort_values(by='Count',ascending=False).head(10)

# Create Pie Chart
pie_visual = go.Pie(labels=df1_sorted['Final Call Distress'], values=df1_sorted['Count'], 
                    marker=dict(colors=px.colors.qualitative.Plotly),
                    textinfo='label+percent', hoverinfo='value', 
                    hole=0.3, pull=[0.1 if i % 2 == 0 else 0 for i in range(len(df1_sorted))])

layout = go.Layout(width=800, height=600,paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777",)
pie_visual_chart = go.Figure(data=[pie_visual], layout=layout)

######################## TAB 2 - CORRELATION MATRIX ########################
data_calltype = fire_incidents

# Exclude non-numeric columns
numeric_df = data_calltype.select_dtypes(include=['number'])

if numeric_df.shape[1] < 2:
    print(f'No correlation plots shown: The number of numeric columns ({numeric_df.shape[1]}) is less than 2')
    

corr = numeric_df.corr()

correlation_plot = px.imshow(corr,
                labels=dict(color="Correlation"),
                x=corr.index,
                y=corr.columns,
                color_continuous_scale="Viridis")

correlation_plot.update_layout(
    width=800,
    height=800,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)

######################## TAB 3 - VIOLIN PLOT ########################

violin_plot = px.violin(fire_violations, x='Status', y='close date')

# Update layout for better visibility
violin_plot.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)

######################## TAB 4 - LINE CHART ########################

# Convert columns to datetime objects
fire_incidents['Alarm DtTm'] = pd.to_datetime(fire_incidents['Alarm DtTm'])
fire_incidents['Arrival DtTm'] = pd.to_datetime(fire_incidents['Arrival DtTm'])

# Calculate the time differences
fire_incidents['Time Difference'] = fire_incidents['Arrival DtTm'] - fire_incidents['Alarm DtTm']

# Calculate the mean time difference
mean_time_difference = fire_incidents['Time Difference'].mean()
# Create a line plot with 'Alarm DtTm' and 'Arrival DtTm'
trace_plot = go.Figure()

# Line for 'Alarm DtTm'
trace_plot.add_trace(go.Scatter(x=fire_incidents.index, y=fire_incidents['Alarm DtTm'],
                         mode='lines', name='Alarm DtTm'))

# Line for 'Arrival DtTm'
trace_plot.add_trace(go.Scatter(x=fire_incidents.index, y=fire_incidents['Arrival DtTm'],
                         mode='lines', name='Arrival DtTm'))

# Fill the space between the lines with different colors
trace_plot.update_layout(shapes=[
    # Highlight the space between the lines with different colors
    go.layout.Shape(
        type='rect',
        xref='x',
        yref='y',
        x0=fire_incidents.index[0],
        y0=0,
        x1=fire_incidents.index[-1],
        y1=mean_time_difference.total_seconds(),
        fillcolor='lightblue',  # Color for the space above the mean time difference
        opacity=0.5,
        layer='below',
        line=dict(width=1),
    ),
    go.layout.Shape(
        type='rect',
        xref='x',
        yref='y',
        x0=fire_incidents.index[0],
        y0=mean_time_difference.total_seconds(),
        x1=fire_incidents.index[-1],
        y1=fire_incidents['Time Difference'].max().total_seconds(),
        fillcolor='lightgreen',  # Color for the space below the mean time difference
        opacity=0.5,
        layer='below',
        line=dict(width=1),
    ),
    
])

# Update the layout for better visibility
trace_plot.update_layout(
    xaxis_title='Index',
    yaxis_title='Time',
    showlegend=True,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)

############################################################### PAGE 4 ###############################################################

######################## TAB 1 - BAR CHART ########################

# Utility Functions

# Utility Function to Create Bar Chart using Plotly Express
def create_bar_chart(data, x_column, y_column):
    """Create a bar chart using Plotly Express."""
    return px.bar(data, x=x_column, y=y_column)

# Data Preparation and Visualization for Tab 1 - Incident Counts by Call Type
call_type_counts_df = df_call_for_service['Call Type'].value_counts().reset_index()
call_type_counts_df.columns = ['Call Type', 'Count']
incident_by_call_type_chart = create_bar_chart(call_type_counts_df, 'Call Type', 'Count')

# Update layout for better visibility
incident_by_call_type_chart.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)

######################## TAB 2 - BAR CHART ########################

# Data Preparation and Visualization for Tab 2 - Incident Counts by Neighborhood District
neighborhood_counts_df = df_call_for_service['Neighborhood  District'].value_counts().reset_index()
neighborhood_counts_df.columns = ['Neighborhood District', 'Count']
incident_by_neighborhood_chart = create_bar_chart(neighborhood_counts_df, 'Neighborhood District', 'Count')

# Update layout for better visibility
incident_by_neighborhood_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)', 
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)


######################## TAB 3 - BAR CHART ########################

# Data Preparation and Visualization for Tab 3 - Average Response Time by Neighborhood District
df_call_for_service['Received DtTm'] = pd.to_datetime(df_call_for_service['Received DtTm'])
df_call_for_service['On Scene DtTm'] = pd.to_datetime(df_call_for_service['On Scene DtTm'])

# Calculate Response Time in minutes
df_call_for_service['Response Time'] = (df_call_for_service['On Scene DtTm'] - df_call_for_service['Received DtTm']).dt.total_seconds() / 60

# Group by neighborhood and calculate the mean response time
response_time_neighborhood_df = df_call_for_service.groupby('Neighborhood  District')['Response Time'].mean().reset_index()

# Visualize the average response time by Neighborhood District using Plotly Express
average_response_time_chart = create_bar_chart(response_time_neighborhood_df, 'Neighborhood  District', 'Response Time')

# Update layout for better visibility
average_response_time_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(gridcolor='lightgray'),
    yaxis=dict(gridcolor='lightgray'),
    font_color="#777"
)