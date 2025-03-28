from src.views.components.buttons.button_style import IStyleButton
from src.views.components.buttons.button_template import button_template


def button_component(title, id, type, style:IStyleButton):
    return button_template(id=id, style=style, type=type, tile=title)
