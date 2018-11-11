# -*- coding: iso-8859-1 -*-
from flask import Flask, render_template, request, session
import os
from model.DB.DB import DB
from controller.controller import Controller

app = Flask(__name__)
controller = Controller()


@app.errorhandler(404)
def not_found(error):
    """Pagina not found."""
    return render_template('not_found.html'), 404


@app.route('/', methods=["GET"])
def index_html(erro=""):
    """Pagina principal da aplicacao."""
    dados = controller.inicio(erro="")
    return render_template('index_html.html', dados=dados)


@app.route('/validar_dados', methods=["POST"])
def validar_dados():
    """Validacao dos inputs."""
    _r = controller.validar()

    raise Exception(request.form.getlist('id_empresa_comp'):)

    if _r[0] == 0:
        return index_html(erro=_r[1])

    dados = controller.calcular(dados=_r[1])

    return 'ljfksdjfsldk'


@app.route('/db')
def db():
    """Teste da conexao com o banco."""
    bd = DB()
    bd.conectar()
    if bd.testar_conexao():
        return "Banco conectado."
    else:
        return "N&atilde;o foi poss&iacute;vel se conectar ao banco."


port = int(os.environ.get('PORT', "5000"))
if __name__ == "__main__":
    # debug=True, use_reloader=True,
    app.run(host='0.0.0.0', port=port, use_reloader=True)
