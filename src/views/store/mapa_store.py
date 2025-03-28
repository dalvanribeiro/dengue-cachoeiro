import pandas as pd
import plotly.express as px

def gerar_mapa(gdf, variavel):
    hidden_bar = 0

    if gdf.crs != 'EPSG:4326':
        gdf = gdf.to_crs('EPSG:4326')


    fig = px.choropleth(
        gdf,
        geojson=gdf.geometry.__geo_interface__,
        locations=gdf.index,
        color=variavel,
        hover_name="Bairro",
        hover_data=[variavel],
        color_continuous_scale="Reds",
        projection="mercator",
    )

    fig.update_geos(fitbounds="locations", visible=False)
    tickvals = []
    if variavel is not None:
        maximo = gdf[variavel].max()
        minimo = gdf[variavel].min()
        if variavel in ['Ano 2022 (absoluto)',
                        'Ano 2023 (absoluto)',
                        'Ano 2024 (absoluto)',
                        'Ano 2022 (Per capita)',
                        'Ano 2023 (Per capita)',
                        'Ano 2024 (Per capita)']:

            medio  = (gdf[variavel].max() - gdf[variavel].min()) / 2
            tickvals = [maximo, medio, minimo]
        if variavel in ['Lixo Coletado','Água da Rede']:
            medio = ((gdf[variavel].max() - gdf[variavel].min()) / 2) + gdf[variavel].min()
            tickvals = [minimo, medio, maximo]

    fig.update_layout(
        coloraxis_colorbar=dict(
            title='',
            tickvals=tickvals,
            ticktext=["Alto", "Médio", "Baixo"],
            orientation='h',
            x=0.5,
            y=-0.1,
            xanchor='center',
            yanchor='top',
            len=0.8,
            thickness= 10
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 50},
        width=400,
        height=350,
    )

    return fig
