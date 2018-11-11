# encoding: iso-8859-1
from model.acoes import Acoes
from flask import request, session


class Controller(object):
    """Controller do sistema."""

    def __init__(self):
        """Inicializa a classe."""
        self.acoes = Acoes()

    def inicio(self, erro=""):
        """Busca os dados da tela inicial."""
        dados = {'empresas': [],
                 "erro": erro.decode('iso-8859-1').encode('utf8')}

        try:
            dados['empresas'] = self.acoes.buscar_empresas()
        except:
            pass

        return dados

    def validar(self):
        """Valida os dados da request."""
        data_inicio = request.form.get('data_init', '')
        if data_inicio:
            _r = self.acoes.validar_data(data_inicio)

            if _r[0]:
                data_inicio = _r[1]
            else:
                return (0, u'Data ínicio inválida')

        data_fim = request.form.get('data_fim', '')
        if data_fim:
            _r = self.acoes.validar_data(data_fim)

            if _r[0]:
                data_fim = _r[1]
            else:
                return (0, u'Data fim inválida.')

        id_empresa = request.form.get('id_empresa', None)
        _r = self.acoes.validar_empresa(id_empresa)

        if _r[0]:
            id_empresa = _r[1]
        else:
            return (0, u'ID(s) empresa(s) inválido')

        id_empresa_comp = request.form.getlist('id_empresa_comp')
        _r = self.acoes.validar_empresa(id_empresa_comp)

        if _r[0]:
            id_empresa_comp = _r[1]
        else:
            return (0, u'ID(s) empresa(s) inválido')

        return (1, {'dt_init': data_inicio, 'id_empresa': id_empresa,
                    'dt_fim': data_fim, 'id_empresa_comp': id_empresa_comp})

    def calcular(self, dados):
        """Calcula a correlacao dos dados."""
        _r = self.acoes.calcular(dados=dados)

        if _r:
            return (1, _r)
        else:
            return (0, _r)
