from src.views.components.buttons.button_component import button_component
from src.views.components.buttons.button_style import ButtonStyleDefault, ButtonStyleCustom
from src.views.components.cards.card_component import card_component
from src.views.components.card_principal.card_principal_component import card_principal_component
from src.views.components.mainbox.main_box_component import main_box_component
from src.views.store.options_store import OptionsStore
from dash import html, dcc
from src.views.utils.img_util import open_img


def home_template(style):
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
                                          className="font-semibold text-purple-700",
                                           href = "/"
                                          ),
                                   html.P("", className="m-2"),
                                   html.A(id="dashbord",children="Visualização",href="/home",className="font-semibold text-gray-500")
                               ]
                           )
                 ]
                 ),
        html.Div(
             className= "sm:row-span-10 flex flex-row sm:col-span-4",
            children= [
                html.Div(
                    className="flex flex-col sm:col-span-2 justify-evenly basis-10/12",
                    children=[
                        html.Div(
                            className="flex flex-row items-end",
                            children=
                            [

                                html.P(className="text-purple-700 text-3xl font-semibold whitespace-pre-line ml-10 mr-10 mt-2 mb-0",
                                       children= "Bem-vindo\nà visualização de \ncasos de dengue do município de\nCachoeiro de Itapemirim"),

                                html.Img(className="w-auto h-64 object-cover ",
                                         src=open_img("src/views/assest/img/picada-de-mosquito.png")),

                            ]
                        ),
                        html.P(className="whitespace-pre-line font-semibold ml-10 mr-10 mt-2 mb-6",
                               children="O mapa interativo permite à Secretaria de Saúde visualizar as regiões com maiores índices de dengue\n e priorizar as intervenções."),
                        html.Div(
                            className="ml-10 mr-10 mt-2 mb-0 ",
                            children= [
                                html.Div( className="basis-9/12"),
                                html.A(className="text-sm",
                                       href="/dash",
                                       children=
                                button_component(type="submit", id='gerar', title="Acessar dashboard",
                                         style=ButtonStyleCustom(style="bg-purple-700 p-3")))]
                        ),



                    ]
                ),
                html.Div(
                    className="flex flex-row basis-2/12 ",
                    children=[
                        html.Div(
                           # className="h-80 w-1 bg-gray-700 m-2"
                        ),
                        html.Div(
                            className="flex items-start flex-col ",
                            children=[
                            html.Img(className="w-auto h-16 object-cover  ml-0 mr-0 mt-20 mb-6",
                                     src=open_img("src/views/assest/img/logo-cachoeiro.png")),
                            html.Div(
                                [
                                    html.P("Conheça o LabCidades",className="font-semibold",),
                                    html.A(className="text-sm",children="labcidades.com.br",href ="https://labcidades.com.br/"),
                                ]
                            ),
                            html.P(className="ml-0 mr-10 mt-10 mb-2 font-semibold",
                                   children="Acompanhe"),
                            html.Div(
                                className="flex flex-row",
                                children=[
                                    html.A(className="text-sm",
                                           href= "https://www.instagram.com/labcidades/",
                                           children=
                                    html.Img(className="w-auto h-7 object-cover",
                                             src=open_img("src/views/assest/img/instagram.png")),
                                           ),
                                    html.Div(className="w-3"),
                                    html.A(className="text-sm",
                                           href=" https://www.linkedin.com/company/ufeslabcidades/",
                                           children=
                                    html.Img(className="w-auto h-7 object-cover",
                                             src=open_img("src/views/assest/img/linkdin.png")),
                                           )
                                ]
                            ),

                            html.P(className="ml-0 mr-10 mt-10 mb-2 font-semibold",
                                   children="Fale conosco"),
                                html.A(className="text-sm",
                                       href="mailto:contato@labcidades.com.br",
                                       children=
                            html.Img(className="w-auto h-7 object-cover",
                                     src=open_img("src/views/assest/img/email.png"))

                                       )]),

                    ]
                ),
            ]
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