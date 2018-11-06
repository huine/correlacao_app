# -*- coding: iso-8859-1 -*-
from model.DB.DB import DB


class Pesquisa(object):
    """Classe responsavel por executar querys."""

    def __init__(self):
        """Inicializa a classe."""
        self.query = None

    def _exec(self):
        """Executa a query que esta no atributo query."""
        self.conexao = DB()
        cur = self.conexao.conectar()
        cur.execute(self.query)
        sql = cur.fetchall()
        cur.close()

        return sql

    def busca_empresa(self, empresas=None):
        """Busca as empresas disponiveis no banco."""
        self.query = """
            SELECT
                *
            FROM
                empresas
            WHERE
                1=1
        """

        if empresas and empresas is not None and len(empresas) > 0:
            tmp = "AND id in (%s)" % (','.join(str(x) for x in empresas))
            self.query += tmp
            tmp = ''

        return self._exec()

    def busca_acoes(self, empresas=None):
        """Busca as empresas disponiveis no banco."""
        query = """
            SELECT
                v.id,
                e.nome,
                v.data,
                v.open,
                v.high,
                v.low,
                v.close,
                v.adj_close,
                v.volume
            FROM
                empresas e
                    INNER JOIN valores v ON v.id_empresa = e.id_empresa
            WHERE
                1=1
        """

        if empresas and empresas is not None and len(empresas) > 0:
            query += (
                ("AND id_empresa in (%s)") % (
                    ','.join(str(x) for x in empresas))
            )

        self.query = query

        return self._exec()
