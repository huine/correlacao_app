# -*- coding: iso-8859-1 -*-
from flask import Flask
from flask import render_template
import os
from model.DB.DB import DB
from controller.controller import Controller

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Pagina not found."""
    return render_template('not_found.html'), 404


@app.route('/', methods=["GET"])
def index_html():
    """Pagina principal da aplicacao."""
    dados = Controller.inicio()
    return render_template('index_html.html', dados=dados)


@app.route('/bd')
def bd():
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
