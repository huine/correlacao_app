# -*- coding: iso-8859-1 -*-
from model.pesquisa.pesquisa_db import Pesquisa


class Acoes(object):
    """Classe objeto acao."""

    def __init__(self):
        """Inicializa o objeto."""
        self._p = Pesquisa()

    def buscar_empresas(self, empresas=[]):
        """Busca as empresas disponiveis no banco."""
        return self._p.busca_empresa(empresas=empresas)

    def buscar_acoes_empresas(self, empresas=[]):
        """Busca as acoes das empresas solicitadas."""
        return self._p.busca_acoes(empresas=empresas)
