import json
from flask import Blueprint, Flask, request, send_file
from business import createImg, deleteFilesRequest, downloadImg
from model import Model
app = Flask(__name__)

prefixed = Blueprint('prefixed', __name__, url_prefix='/api/v1')

@prefixed.route('/')
def index():
    return '''
    <h1> Welcome to the LastCollageFm API!</h1>
    <a href='https://github.com/vlopess/MyCollageFm-API'>Read the documentation!</a>
    '''

@prefixed.route('/generateCollage', methods=['POST'])
def generateCollage():       
    dados = request.form['data']
    dados = Model.from_map(json.loads(dados))
    downloadImg(dados)
    filename = createImg(dados)
    file = send_file(filename)
    deleteFilesRequest(dados.id)
    return file, 200

app.register_blueprint(prefixed)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
