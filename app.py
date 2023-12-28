import json
from flask import Flask, jsonify, request, send_file

from business import createImg, deleteFilesRequest, downloadImg
from model import Model

app = Flask(__name__)

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
