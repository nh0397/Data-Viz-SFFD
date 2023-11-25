# app.py
from dash import Dash, Output, Input
from appshell.appshell import create_appshell
from appshell.appshell import display_page  # Correct the import
from controller.controller import Controller

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    use_pages=True,
    update_title=None,
)

controller = Controller()
controller.configure()

app.layout = create_appshell(app)
server = app.server

# Move callback registration here
app.callback(Output("page-content", "children"), Input("url", "pathname"))(display_page)

if __name__ == "__main__":
    app.run_server(debug=True)
