from dash import html

from src.views.components.buttons.button_style import IStyleButton


def button_template(tile, id, style:IStyleButton, type):
    print(id,style.setButtonStyle())
    button = html.Button(tile,
                         id=id,
                         className=style.setButtonStyle(),
                         type=type)
    return button
