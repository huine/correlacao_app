# -*- coding: iso-8859-1 -*-
from model.pesquisa.pesquisa_db import Pesquisa
from datetime import datetime


class Acoes(object):
    """Classe objeto acao."""

    def __init__(self):
        """Inicializa o objeto."""
        self._p = Pesquisa()

    def buscar_empresas(self, empresas=[]):
        """Busca as empresas disponiveis no banco."""
        return self._p.busca_empresa(empresas=empresas)

    def buscar_acoes_empresas(self, empresas=[], dt_init=None, dt_fim=None):
        """Busca as acoes das empresas solicitadas."""
        return self._p.busca_acoes(empresas=empresas, dt_init=dt_init,
                                   dt_fim=dt_fim)

    def validar_data(self, data):
        """Valida uma data e retorna como objeto Date."""
        d = None
        try:
            if data:
                d = datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            return (0, d)
        
        return (1, d)

    def validar_empresa(self, id_empresa, unique=False):
        """Valida o id_empresa e retorna uma lista de int."""
        try:
            if not unique:
                if len(id_empresa) == 0:
                    return (0, [])

                if isinstance(id_empresa, (list, tuple)):
                    return (1, [int(x) for x in id_empresa])
                else:
                    return (1, [int(x)])
            else:
                return (1, int(id_empresa))
        except:
            if not unique:
                return (0, [])
            else:
                return (0, None)

    def calcular(self, dados):
        """Recebe os dados necessarios para iniciar os calculos."""
        emp_princ = self.acoes.busca_acoes(
            empresas=dados['id_empresa'], dt_init=dados['dt_init'],
            dt_fim=dados['dt_fim'])

        raise Exception(emp_princ)
        
