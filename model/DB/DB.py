# -*- coding: iso-8859-1 -*-
import os
import psycopg2
import psycopg2.extras


class DB(object):
    """Classe que controla o acesso ao banco."""

    def __init__(self):

        dbname = os.environ["DATABASE_NAME"]
        dbpswd = os.environ["DATABASE_PSWD"]
        dbuser = os.environ["DATABASE_USER"]

        self.conexao = (
            ('dbname=%s user=%s password=%s host=127.0.0.1 port=5432') % (
                dbname, dbuser, dbpswd)
        )

        self.conector = None

    def get_conector(self):
        """Retorna o conector."""
        return self.conector

    def conectar(self):
        """Realiza a conexao com o banco."""
        try:
            self.conector = psycopg2.connect(self.conexao)
            return self.conector.cursor(
                cursor_factory=psycopg2.extras.DictCursor)
        except Exception, e:
            print('Erro ao conectar no banco, erro: %s' % e)

    def testar_conexao(self):
        """Teste da conexao."""
        if self.conector is None or self.conector.closed:
            return False
        else:
            return True

        self.conector.close()
