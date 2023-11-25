from dash import Dash, dcc, html, callback, Output, Input
from dash.dependencies import State
import plotly.express as px
import dash

# Sample data for demonstration
iris = px.data.iris()

# Create a Dash app
app = Dash(__name__, external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"])

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', style={'width': '100%', 'height': '100vh', 'position': 'absolute'}),
])

# Define the HTML template
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    <!-- Add Plotly library -->
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <title>FlareGraph</title>
</head>
<body>

    <nav class="navbar">
        <div class="logo">
            <img src="assets/logo.png" alt="Logo">
        </div>
        <div class="navbar-header">
            <h1 id="headerText">FlareGraph: Exploring Fire Department Statistics in San Francisco</h1>
        </div>
        <div class="contact-icons">
            <a href="#" class="icon"><img src="assets/home.png" alt="Logo"></a> 
        </div>
    </nav>

    <div class="content">
        <div class="sidenav" id="sidenav">
            <button class="collapse-btn" onclick="toggleSidebar()">☰</button>
            <div class="sidebar-content">
                <button onclick="displayPlot('section1')">
                    <i class="fas fa-home"></i><span class="nav-text">Section 1</span>
                </button>
                <button onclick="displayPlot('section2')">
                    <i class="fas fa-star"></i><span class="nav-text">Section 2</span>
                </button>
                <button onclick="displayPlot('section3')">
                    <i class="fas fa-cogs"></i><span class="nav-text">Section 3</span>
                </button>
            </div>
        </div>

        <!-- Sections for Dash components -->
        <div id="section1" class="section">
            {%app_entry%}
        </div>
        <div id="section2" class="section">
            <!-- Dash component goes here -->
        </div>
        <div id="section3" class="section">
            <!-- Dash component goes here -->
        </div>
    </div>

    <script>
        function toggleSidebar() {
            const sidebar = document.getElementById('sidenav');
            sidebar.classList.toggle('collapsed');
        }

        function displayPlot(sectionId) {
            // Clear previous content
            document.getElementById(sectionId).innerHTML = "";

            // Create a sample Plotly plot (replace this with your actual plots)
            const data = [{ x: [1, 2, 3, 4], y: [10, 11, 12, 13], type: 'scatter' }];
            Plotly.newPlot(sectionId, data);
        }
    </script>

</body>
</html>
"""

# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/section1':
        # Replace this with your Dash component for Section 1
        return dcc.Graph(figure=px.scatter(iris, x='sepal_width', y='sepal_length', color='species'))
    elif pathname == '/section2':
        # Replace this with your Dash component for Section 2
        return dcc.Graph(figure=px.bar(iris, x='species', y='petal_width'))
    elif pathname == '/section3':
        # Replace this with your Dash component for Section 3
        return dcc.Graph(figure=px.pie(iris, names='species'))

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
