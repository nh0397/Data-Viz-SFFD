# pages/home/homepage.py
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html
from dash import dcc
from pages.home.sidebar import layout as sidebar_layout  # Import the sidebar layout
from pages.load_data import fire_incidents,fire_violations
from pages.load_data import fire_incidents



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


layout = html.Div(
    [
        html.Div(
            sidebar_layout,
            style={"width": "5%", "float": "left", "height": "calc(100vh - 100px)"},
        ),
        html.Div(
            [
                html.H1("Welcome to the page3", style={"color": "rgb(255, 107, 107)", "text-align": "center"}),
                # Add other components as needed
            ],
            style={"width": "95%", "float": "left", "height": "calc(100vh - 100px)", "padding": "20px"},
        ),
        dcc.Graph(
            id='example-graph7',
            figure=fig2
        ),
        dcc.Graph(
            id='example-graph8',
            figure=fig3
        ),
        dcc.Graph(
            id='example-graph9',
            figure=fig4
        ),
        dcc.Graph(
            id='example-graph10',
            figure=fig1
        )

    ],
    style={"margin-top": "100px"},
)
