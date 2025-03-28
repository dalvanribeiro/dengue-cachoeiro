import pandas as pd


class OptionsStore():
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
    def preencher_options_variaveis(self) -> list:
        options_escola = []
        escolas = self.dataframe["Escola"].unique().tolist()
        for escola in escolas:
            options_escola.append({'label': '%s' % escola, 'value': '%s' % escola})
        return options_escola
    def preencher_options_turmas(self) -> list:
        options_turmas = []
        turmas = self.dataframe["Turmas"].unique().tolist()
        for turma in turmas:
            options_turmas.append({'label': '%s' % turma, 'value': '%s' % turma})
        return options_turmas
    def preencher_options_datas(self) -> list:
        options_dias = []
        dias = self.dataframe["Dia"].unique().tolist()
        for dia in dias:
            options_dias.append({'label': '%s'%dia, 'value': '%s'%dia})
        return options_dias



