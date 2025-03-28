from src.views.pages.home.home_template import home_template
from src.views.pages.home.home_style import home_style
from src.views.store.options_store import OptionsStore
def home_page():
    style = home_style()
    return home_template(style=style)