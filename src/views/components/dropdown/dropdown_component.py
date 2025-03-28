from dash import dcc
from src.views.components.dropdown.dropdown_style import dropdown_style
from src.views.components.dropdown.dropdown_template import dropdown_template


def dropdown_component(options_data,id,placeholder):
    style_dropdown = dropdown_style()
    return dropdown_template(options_data=options_data, style_dropdown=style_dropdown,id=id ,placeholder=placeholder)
