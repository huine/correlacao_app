# -*- coding: iso-8859-1 -*-
import os
import sqlalchemy as sql


class DB(object):
    """Classe que controla o acesso ao banco."""

    def __init__(self):
        """."""
        dbname = os.environ["DATABASE_NAME"]
        dbpswd = os.environ["DATABASE_PSWD"]
        dbuser = os.environ["DATABASE_USER"]

        self.conexao = (
            ("postgres://%s:%s@localhost:5432/%s") % (dbuser, dbpswd, dbname)
        )

        self.conector = sql.create_engine(self.conexao)

    def get_conector(self):
        """Retorna o conector."""
        return self.conector

    def testar_conexao(self):
        """Teste da conexao."""
        if self.conector and self.conector.execute(
                """SELECT 1 AS is_alive"""):
            return True
        else:
            return False
