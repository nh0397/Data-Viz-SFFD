# data_loader.py
import pandas as pd
import plotly.express as px
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df_call_for_service = pd.read_csv('./Data/SF_FD.csv', low_memory = False)
fire_incidents = pd.read_csv("./Data/Fire_Incidents.csv", low_memory = False)
fire_violations = pd.read_csv("./Data/Fire_Violations_20231011.csv")

# PAGE 5 Data 



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


# Page 3 data
# Group by district and calculate the total count of violation codes
district_counts = fire_violations.groupby('neighborhood district')['violation item'].count().reset_index(name='count')

# Sort districts based on the total count in descending order
district_counts_sorted = district_counts.sort_values(by='count', ascending=False)

# Display the top three districts
top_three_districts = district_counts_sorted.head(3)
#have to print the top three districts with most number of violation codes.
ttd = pd.DataFrame(top_three_districts)


# Assuming 'fire_violations' is your DataFrame

# Function to plot histograms
df = fire_violations
n_histogram_shown=10
n_histogram_per_row=3

nunique = df.nunique()
df = df[[col for col in df if 1 < nunique[col] < 50]]  # Filter columns with 1 to 50 unique values
column_names = list(df)
n_row, n_col = df.shape
n_hist_row = (n_col + n_histogram_per_row - 1) // n_histogram_per_row
    
# Create a subplot grid
fig2 = make_subplots(rows=n_hist_row, cols=n_histogram_per_row,
                    subplot_titles=[f'{column_names[i]} (column {i})' for i in range(n_col)])
    
# Populate subplots with histograms
for i in range(n_col):
    row = (i // n_histogram_per_row) + 1
    col = (i % n_histogram_per_row) + 1
    fig2.add_trace(go.Histogram(x=df.iloc[:, i], nbinsx=30),  # Use nbinsx instead of nbins
                  row=row, col=col)
    
# Update layout for better visibility
fig2.update_layout(height=n_hist_row * 400, width=n_histogram_per_row * 500,
                  showlegend=False, title_text="Histograms of Fire Violations Data",
                  template="plotly_white")
    


#############
# Assuming 'fire_incidents' is your DataFrame
df2 = fire_incidents

# Correlation matrix

# Exclude non-numeric columns
numeric_df = df2.select_dtypes(include=['number'])

if numeric_df.shape[1] < 2:
    print(f'No correlation plots shown: The number of numeric columns ({numeric_df.shape[1]}) is less than 2')
    

corr = numeric_df.corr()

fig3 = px.imshow(corr,
                labels=dict(color="Correlation"),
                x=corr.index,
                y=corr.columns,
                color_continuous_scale="Viridis",
                title='Correlation Matrix')

# Update layout for better visibility
fig3.update_layout(width=800, height=800)


# Call the function to plot the correlation matrix

###############
# Convert closing_date to datetime object
fire_violations['close date'] = pd.to_datetime(fire_violations['close date'])

fig4 = px.violin(fire_violations, x='Status', y='close date', title='Closing Dates by Status (Violin Plot)')

# Convert columns to datetime objects
fire_incidents['Alarm DtTm'] = pd.to_datetime(fire_incidents['Alarm DtTm'])
fire_incidents['Arrival DtTm'] = pd.to_datetime(fire_incidents['Arrival DtTm'])

# Calculate the time differences
fire_incidents['Time Difference'] = fire_incidents['Arrival DtTm'] - fire_incidents['Alarm DtTm']

# Calculate the mean time difference
mean_time_difference = fire_incidents['Time Difference'].mean()
# Create a line plot with 'Alarm DtTm' and 'Arrival DtTm'
fig1 = go.Figure()

# Line for 'Alarm DtTm'
fig1.add_trace(go.Scatter(x=fire_incidents.index, y=fire_incidents['Alarm DtTm'],
                         mode='lines', name='Alarm DtTm'))

# Line for 'Arrival DtTm'
fig1.add_trace(go.Scatter(x=fire_incidents.index, y=fire_incidents['Arrival DtTm'],
                         mode='lines', name='Arrival DtTm'))

# Fill the space between the lines with different colors
fig1.update_layout(shapes=[
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
    )
])

# Update the layout for better visibility
fig1.update_layout(title='Time Difference between Alarm and Arrival',
                  xaxis_title='Index',
                  yaxis_title='Time',
                  showlegend=True)

# Page 1 code

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

# df_call_for_service = pd.read_csv('./Data/SF_FD.csv', low_memory = False)

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


# Page 2 content 
# Convert the column to datetime if it's not already in datetime format
fire_incidents['Incident Date'] = pd.to_datetime(fire_incidents['Incident Date'])

# Group by date and count occurrences
df_grouped_2 = fire_incidents.groupby(fire_incidents['Incident Date'].dt.date).size().reset_index(name='Frequency')

# Create area chart
fig_timeseries = px.area(df_grouped_2, x='Incident Date', y='Frequency', labels={'Incident Date': 'Incident Date', 'Frequency': 'Number of Fire Incidents'}, title='Time Series Area Chart')