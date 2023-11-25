# controller/controller.py
import dash
from pages.home.homepage import layout as homepage_layout
from pages.page1 import layout as page1_layout

class Controller:
    def configure(self):
        # Register the homepage
        dash.register_page(
            "home",
            path='/',
            title='FlareGraph',
            name='FlareGraph',
            layout=homepage_layout
        ),
        dash.register_page(
            "page1",
            path='/page1',
            title='FlareGraph',
            name='FlareGraph',
            layout=page1_layout
        )
