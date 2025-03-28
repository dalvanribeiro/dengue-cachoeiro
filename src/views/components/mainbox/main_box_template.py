from dash import dcc, html
import plotly.express as px
import pandas as pd
import geopandas as gpd
from dash.dependencies import Input, Output

from src.views.components.dropdown.dropdown_component import dropdown_component
from src.views.components.maps import map_component


def main_box_template(id, style):
    return html.Div(
        children=[

            html.Div(
                children=[
                    # Dropdown e Mapa 1
                    map_component.build(id_map='mapa-dengue',title= 'Casos Dengue', component=dropdown_component(options_data=[
                        'Ano 2022 (absoluto)',
                        'Ano 2023 (absoluto)',
                        'Ano 2024 (absoluto)',
                        'Ano 2022 (Per capita)',
                        'Ano 2023 (Per capita)',
                        'Ano 2024 (Per capita)'
                    ], placeholder='Selecione a variável:', id="variavel_dengue"), ),
                    map_component.build(id_map='mapa-agua',title= 'Distribuição de Água', component=dropdown_component(options_data=[
                        'Ano 2010'
                        #'Água da Rede',
                        #'Água de Poço',
                        #'Outras Águas'
                    ], placeholder='Selecione a variável:', id="variavel_agua"), ),
                    map_component.build(id_map='mapa-lixo',title= 'Lixo Coletado', component=dropdown_component(options_data=[
                        'Ano 2010'
                        #'Lixo Coletado',
                        #'Lixo Queimado',
                        #'Lixo Enterrado',
                        #'Lixo em Terreno',
                        #'Lixo em Rios',
                        #'Outros Lixos'
                    ], placeholder='Selecione a variável:', id="variavel_lixo"), ),

                ],
                style={
                    'display': 'flex',
                    'justify-content': 'space-between',
                    'flex-wrap': 'wrap'
                }
            )
        ]
    )
