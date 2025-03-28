from dash import dcc


def dropdown_template(options_data, style_dropdown,placeholder,id) -> dcc:
    template = dcc.Dropdown(
        id=id,
        style=style_dropdown,
        options=options_data,
        placeholder=placeholder,
    )
    return template

