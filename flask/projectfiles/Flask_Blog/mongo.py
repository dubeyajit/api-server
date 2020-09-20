from flask import Flask 
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import simplejson as json
import secrets
from datetime import datetime
#from simplejson import json

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://ajitdubey:poiuytre@172.17.0.2:27017/gnuhealth'

mongo = PyMongo(app)

bcrypt = Bcrypt()

@app.route('/user', methods=['GET'])
def get_all_users():
    user = mongo.db.users
    output = []
    for s in user.find():
        output.append({'name' : s['name'], 'email' : s['email'], 'password' : s['password']})
    return jsonify({'result' : output})

@app.route('/user/<name>', methods=['GET'])
def get_one_user(name):
    user = mongo.db.users
    s = user.find_one({'name' : name})
    if s:
        output = {'name' : s['name'], 'email' : s['email']}
    else:
        output = "No such user"
    return jsonify({'result' : output})
    
@app.route('/user', methods=['POST'])
def add_user():
    user = mongo.db.users
    name = request.json['name']
    password = request.json['password']
    email = request.json['email']
    pwd_hash = bcrypt.generate_password_hash(password)
    accessToken = secrets.token_hex(32)
    timeStamp = datetime.now()
    #print(pwd_hash)
    #output = {'name' : name, 'password' : pwd_hash}
    user_id = user.insert({'name' : name, 'email' : email, 'password' : pwd_hash, 'accessToken' : accessToken, 'timeStamp' : timeStamp})
    new_user = user.find_one({'_id': user_id})
    output = {'name' : new_user['name'], 'email' : new_user['email'], 'password' : new_user['password'], 'accessToken' : new_user['accessToken'], 'timeStamp' : new_user['timeStamp']}
    return jsonify({'result' : output})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')