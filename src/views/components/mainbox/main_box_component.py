from src.views.components.mainbox.main_box_template import main_box_template
from src.views.components.mainbox.main_box_style import main_box_style
def main_box_component(id):
    style = main_box_style()
    return main_box_template(id=id,style=style)