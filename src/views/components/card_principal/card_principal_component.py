from src.views.components.card_principal.card_principal_style import card_principal_style
from src.views.components.card_principal.card_principal_template import card_principal_template
def card_principal_component(options_variavel_1 : list[str], options_variavel_2:list[str]):
    style = card_principal_style()
    return card_principal_template(options_variavel_1 , options_variavel_2,style)