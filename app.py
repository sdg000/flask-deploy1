# import os

# from flask import Flask, jsonify, make_response
# from flask_migrate import Migrate
# from flask_restful import Api, Resource


# from model import db, Bird

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# migrate = Migrate(app, db)
# db.init_app(app)

# api = Api(app)


# # adding a custom non-restful route
# @app.route('/')
# def home():
#     # return {'message': 'welcome to homepage'}, 200
#     return '<h1>Welcome to my page!</h1>'

# class Birds(Resource):

#     def get(self):
#         birds = [bird.to_dict() for bird in Bird.query.all()]
#         return make_response(jsonify(birds), 200)

# api.add_resource(Birds, '/birds')



from flask import request, session
from flask_restful import Resource
from flask import Flask, jsonify, make_response


from model import Bird
from config import db, api, app

# adding a custom non-restful route
@app.route('/')
def home():
    # return {'message': 'welcome to homepage'}, 200
    return '<h1>Welcome to my page!</h1>'

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)
    

# Resource for Deleting , Updating or getting Bird by ID
class BirdByID(Resource):

    def get(self, id):
        bird = Bird.query.filter(Bird.id == id).first()
        if bird:
            return bird.to_dict(), 200
        
        return {'message': 'Not found'}, 401

api.add_resource(Birds, '/birds')
api.add_resource(BirdByID, '/birds/<int:id>')



