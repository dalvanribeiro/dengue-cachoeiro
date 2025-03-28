from src.views.pages.dash.dash_template import dash_template
from src.views.pages.dash.dash_style import dash_style
from src.views.store.options_store import OptionsStore
def dash_page(option:OptionsStore=None):
    style = dash_style()
    return dash_template(style=style)