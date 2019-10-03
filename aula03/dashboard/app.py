
import os
import sys

import flask

from routes.docker import blueprint as docker
from routes.jenkins import blueprint as jenkins
from routes.auth import blueprint as auth
from routes.gitlab import blueprint as gitlab


app = flask.Flask(__name__)

app.secret_key =  'secret'

app.register_blueprint(docker)
app.register_blueprint(jenkins)
app.register_blueprint(auth)
app.register_blueprint(gitlab)

#aqui só pode ser configuração, nada de lógica

if __name__ == "__main__":
    app.run()
