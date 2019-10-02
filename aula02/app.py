
import bson
import flask
import pymongo 

app = flask.Flask(__name__)

client = pymongo.MongoClient()
db = client.coffee # use coffee


@app.errorhandler(404)
def handler_404(err):
    return '#FODA-SE'

@app.route('/hello-world')
def get_hello_world():
    return 'hello, world'

@app.route('/users', methods= [ 'GET' ])
def get_users():
    
    users = [{
        'id': str(u.get('_id')),
        'name': u.get('name'),
        'email': u.get('email'),
        'password': u.get('password')
    } for u in db.users.find() ]
    
    return flask.jsonify(users)

@app.route('/users', methods = [ 'POST' ])
def create_user():
    
    db.users.insert(flask.request.json)
    
    return flask.jsonify({ 
        'mensagem' : 'usuario cadastrado'
    })

@app.route('/users/<userid>', methods = [ 'GET' ])
def get_user_by_id(userid):
    
    user = db.users.find_one({
        '_id': bson.ObjectId(userid)
    })
    
    return flask.jsonify({
        'id': str(user.get('_id')),
        'name': user.get('name'),
        'email': user.get('email'),
        'password': user.get('password')
    })
    
@app.route('/users/<userid>', methods=[ 'PUT', 'PATCH'])
def update_user_by_id(userid):
    return 'update user with id {}'.format(userid)
    
@app.route('/users/<userid>', methods= [ 'DELETE' ])
def delete_user_by_id(userid):
    return 'delete user with id {}'.format(userid) 

@app.route('/soma', methods = [ 'POST' ])
def soma():
    numeros = flask.request.json.get('numeros')
    
    if not numeros:
        return 'Chave "números" não encontrada', 400
        
    if  type(numeros) is not list:
        return 'numeros, deve ser uma lista', 400
    
    return flask.jsonify({
        'soma': sum(numeros)
    }), 200
    
    

if __name__ == '__main__':
    app.run(debug=True)
