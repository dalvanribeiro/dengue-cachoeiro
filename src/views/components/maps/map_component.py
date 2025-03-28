from dash import dcc, html

from src.views.components.dropdown.dropdown_component import dropdown_component


def build(id_map:str, title:str, component:dcc):
    return html.Div(
                    children=[
                            title,
                            component,
                            html.Br(),
                            dcc.Graph(
                                id=id_map,
                                # figure=fig,
                            ),
                        ],
                        style={'width': '32%', 'display': 'inline-block'}
                    )