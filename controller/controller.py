# -*- coding: iso-8859-1 -*-
from model.acoes import Acoes


class Controller(object):
    """Controller do sistema."""

    def __init__(self):
        """Inicializa a classe."""
        self.acoes = Acoes()

    def inicio(self):
        """Busca os dados da tela inicial."""
        dados = {'empresas': []}

        try:
            dados['empresas'] = self.acoes.buscar_empresas()
        except:
            pass

        return dados
