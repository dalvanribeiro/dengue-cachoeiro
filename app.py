from src.views.pages.dash.dash_page import dash_page
from src.views.pages.home.home_page import home_page

from dash import Dash, Output, Input,dcc, html
import geopandas as gpd
from src.views.store.mapa_store import gerar_mapa

gdf = gpd.read_file(r'src/data/raw/dados.geojson')
gdf.rename(columns={
        'nome': 'Bairro',
        'Casos_2022': 'Ano 2022 (absoluto)',
        'Casos_2023': 'Ano 2023 (absoluto)',
        'Casos_2024': 'Ano 2024 (absoluto)',
        'Lixo_Colet': 'Lixo Coletado',
        'Lixo_Queim': 'Lixo Queimado',
        'Lixo_Enter': 'Lixo Enterrado',
        'Lixo_terre': 'Lixo em Terreno',
        'Lixo_em_ri': 'Lixo em Rios',
        'Lixo_Outro': 'Outros Lixos',
        'Água_Rede': 'Água da Rede',
        'Água_de_P': 'Água de Poço',
        'Água_Outr': 'Outras Águas',
        'População Por Bairro_População Total':'pop_total'
    }, inplace=True)
gdf['Lixo Coletado'] = gdf['Lixo Coletado'] * (-1)
gdf['Água da Rede'] = gdf['Água da Rede'] * (-1)
gdf['Ano 2022 (Per capita)'] = gdf['Ano 2022 (absoluto)'] / gdf['pop_total']
gdf['Ano 2023 (Per capita)'] = gdf['Ano 2023 (absoluto)'] / gdf['pop_total']
gdf['Ano 2024 (Per capita)'] = gdf['Ano 2024 (absoluto)'] / gdf['pop_total']

external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]
app = Dash(__name__,
           external_scripts=external_scripts,
           suppress_callback_exceptions=True
           )

app.layout = html.Div( id='page-content',children=dcc.Location(id='url', refresh=False))



@app.callback(
Output('mapa-dengue', 'figure'),
    Input('variavel_dengue', 'value')

)
def criar_mapa_dengue(variavel):
    return gerar_mapa(gdf,variavel)
@app.callback(
Output('mapa-agua', 'figure'),
    Input('variavel_agua', 'value')
)
def criar_mapa_agua(variavel):
    if variavel == 'Ano 2010':
        return gerar_mapa(gdf, 'Água da Rede')
    return gerar_mapa(gdf, None)
@app.callback(
Output('mapa-lixo', 'figure'),
    Input('variavel_lixo', 'value')
)
def criar_mapa_lixo(variavel):
    if variavel == 'Ano 2010':
        return gerar_mapa(gdf, 'Lixo Coletado')
    return gerar_mapa(gdf, None)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    dash_page()
    if pathname == '/':
        return home_page()
    if pathname == '/dash':
        return dash_page()
    else:
        return dash_page()


if __name__ == "__main__":
    app.run_server(debug=False,host='0.0.0.0', port=8050)
