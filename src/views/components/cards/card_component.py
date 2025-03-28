from src.views.components.cards.card_template import card_template
from src.views.components.cards.card_style import card_style


def card_component(card_title, id,valor):
    cardstyle = card_style()
    return card_template(card_title=card_title, id=id ,styles=cardstyle,valor_inicial=valor)
