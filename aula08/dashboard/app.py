
import os
import sys
import logging
import flask

from routes.docker import blueprint as docker
from routes.jenkins import blueprint as jenkins
from routes.auth import blueprint as auth
from routes.gitlab import blueprint as gitlab


logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s [ %(levelname)s ] %(name)s ' +
        '[ %(funcName)s ] [ %(filename)s, %(lineno)s] %(message)s',
        datefmt= '[%d/%m/%Y %H:%M:%S ]'
)


app = flask.Flask(__name__)

app.secret_key =  'secret'

logging.info('Iniciando a aplicação...')

@app.errorhandler(404)
def handle_404(err):
    return flask.render_template('404.html')

@app.route('/', methods= [ 'GET' ])
def get_home():
    return flask.redirect('/docker')

app.register_blueprint(docker)
app.register_blueprint(jenkins)
app.register_blueprint(auth)
app.register_blueprint(gitlab)

#aqui só pode ser configuração, nada de lógica

if __name__ == "__main__":
    app.run(host='0.0.0.0')
