# components/my_component.py
from dash import html


def card_template(card_title, id, styles: list,valor_inicial):
    return html.Div([
        html.P(card_title, className=styles[0],style= {
                     "color":  "#64748B"
                 }),
        html.P( valor_inicial, id=id, className=styles[1],style= {
                     "color":  "#64748B",

                 })
    ], className=styles[2])
