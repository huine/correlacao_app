# -*- coding: iso-8859-1 -*-
from model.DB.DB import DB


class Pesquisa(object):
    """Classe responsavel por executar querys."""

    def __init__(self):
        """Inicializa a classe."""
        self.query = None

    def _exec(self):
        """Executa a query que esta no atributo query."""
        conexao = DB()

        _results = conexao.conector.execute(self.query)

        _r = []
        for item in _results:
            _r.append(item)

        return _r

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

    def busca_acoes(self, empresas=None, dt_init=None, dt_fim=None):
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
                    INNER JOIN valores v ON v.id_empresa = e.id
            WHERE
                1=1
        """

        if empresas and empresas is not None and len(empresas) > 0:
            query += (
                ("AND v.id_empresa in (%s)") % (
                    ','.join(str(x) for x in empresas))
            )
        if dt_init:
            query += (
                ("AND v.data >= to_date('%s', 'dd/mm/yyyy')") % (
                    dt_init.strftime('%d/%m/%Y'))
            )

        if dt_fim:
            query += (
                ("AND v.data <= to_date('%s', 'dd/mm/yyyy')") % (
                    dt_fim.strftime('%d/%m/%Y'))
            )

        query += "ORDER BY v.data ASC"

        self.query = query

        return self._exec()
