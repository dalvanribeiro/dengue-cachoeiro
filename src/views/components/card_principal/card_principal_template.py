from dash import html, dcc

from src.views.components.buttons.button_style import ButtonStyleDefault, ButtonStyleCustom
from src.views.components.dropdown.dropdown_component import dropdown_component
from src.views.components.buttons.button_component import button_component




def card_principal_template(options_variavel_1 : list[str], options_variavel_2:list[str],style:list[str]):
    return html.Div([
        html.Div(
            className= "flex item-center  justify-start p-3",
        children= [html.P("Filtrar por :",
               className="text-lg")],style= {
                     "color":  "#64748B"
                 }),

        dropdown_component(options_data=options_variavel_1,placeholder='Ano Dengue:',id="variavel_1"),
        html.Br(),
        dropdown_component(options_data=options_variavel_2, placeholder='Variaveis relacionadas:', id="variavel_2"),
        html.Br(),
        #dropdown_component(options_data=options_data, placeholder='Data final:', id="data-final"),
        html.Br(),




    ], className=style[1])
