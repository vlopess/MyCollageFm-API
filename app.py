import json
from flask import Flask, jsonify, request, send_file

from business import createImg, deleteFilesRequest, downloadImg
from model import Model
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
app.config["APPLICATION_ROOT"] = "/api/v1"
app.wsgi_app = DispatcherMiddleware(app, {'/api/v1': app.wsgi_app})

@app.route('/generateCollage', methods=['POST'])
def generateCollage():       
    dados = request.form['data']
    dados = Model.from_map(json.loads(dados))
    downloadImg(dados)
    filename = createImg(dados)
    file = send_file(filename)
    deleteFilesRequest(dados.id)
    return file, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
