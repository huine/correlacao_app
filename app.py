# -*- coding: iso-8859-1 -*-
# from flask import request
# from flask import current_app
# from flask import jsonify
# from flask import make_response
# from flask import json
# import time
from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """Pagina not found."""
    return render_template('not_found.html'), 404


@app.route('/', methods=["GET"])
@app.route('/<var>', methods=["POST", "GET"])
def index_html(var='Não informado'):
    """Pagina principal da aplicacao."""
    return render_template('index_html.html', var=var)


port = int(os.environ.get('PORT', "5000"))
if __name__ == "__main__":
    # debug=True, use_reloader=True,
    app.run(host='0.0.0.0', port=port)
