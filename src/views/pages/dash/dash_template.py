from src.views.components.buttons.button_component import button_component
from src.views.components.buttons.button_style import ButtonStyleDefault, ButtonStyleCustom
from src.views.components.cards.card_component import card_component
from src.views.utils.img_util import open_img
from src.views.components.card_principal.card_principal_component import card_principal_component
from src.views.components.mainbox.main_box_component import main_box_component
from src.views.store.options_store import OptionsStore
from dash import html, dcc


def dash_template(style,options:OptionsStore=None):
    template = html.Div(
        id = "page",
        children=
        [
             html.Div(className="""sm:row-span-1 sm:col-span-4 p-3 sm:bg-white
                                   flex flex-row items-center  justify-between row-span-2 col-span-4""",
                 children=[html.Img(src= open_img("src/views/assest/img/logo-cachoeiro.png"),
                                  className="w-auto h-12 object-cover"),
                           html.Div(
                               className="flex flex-row",
                               children=[
                                   html.A(id="sobre",
                                          children="Sobre",
                                          className="font-semibold text-gray-500",
                                           href = "/"
                                          ),
                                   html.P("", className="m-2"),
                                   html.A(id="dashbord",children="Visualização",href="/dash",className="font-semibold text-purple-700")
                               ]
                           )
                 ]
                 ),
        html.Div(className="""sm:row-span-1 sm:col-span-4 p-4 sm:bg-gray-100
       #                         flex flex-row items-center justify-between row-span-1 col-span-4""",
                 children=[html.P("Visualização da Dengue em Cachoeiro de Itapemirim ",
                                  className=" text-[20px] font-bold m-3",style={
                     "color":  "#AF23AF"
                  }),

                           html.Div(
                               className="flex flex-row",
                               children=[html.P("", className="m-2"),
                                ]),


                           ]
                 ),

        html.Div(className="""flex  col-span-8 sm:row-span-9 sm:col-span-4
                              p-3 bg-white  shadow-lg flex flex-col items-center
                              row-span-2 col-span-8 m-2""",
                 children=[
                           main_box_component(id="card-grafico")]

                 ),

        html.Div(className="""sm:row-span-1 sm:col-span-4 p-3 
      #                         flex flex-col items-center justify-center row-span-1 col-span-4""",
                 children=[html.P("LabCidades Projetos Inteligentes- Universidade Federal do Espírito Santo (UFES), Goiabeiras, Vitória - ES, 29075-053",
                                  className="text-white text-sm m-3"),
                           ],
                 style= {
                     "background-color":  "#6E6E6E"
                 }

                 ),


    ], className=style,
        )
    return template