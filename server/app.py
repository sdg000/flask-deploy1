# from flask import request, session, make_response, jsonify
# from flask_restful import Resource


# from config import app, db, api
# from model import Bird


# class Birds(Resource):

#     def get(self):
#         birds = [bird.to_dict() for bird in Bird.query.all()]
#         return make_response(jsonify(birds), 200)

# api.add_resource(Birds, '/birds')


import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from model import db, Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tiam1:8SFov96XNa98pwMNlTHGPYSRmvzzGgtb@dpg-ckkjd16a18fc73adl8i0-a.oregon-postgres.render.com/fd1'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# adding a custom non-restful route
@app.route('/')
def home():
    return {'message': 'welcome to homepage'}, 200
    # return '<h1>Welcome to my page!</h1>'

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Birds, '/birds')