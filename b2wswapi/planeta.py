from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from b2wswapi.swapi import SWAPI
from b2wswapi.exceptions.invalid_input import InvalidInput
from b2wswapi.exceptions.swapi_notfound import SWAPINotFound

mongo = PyMongo()

class Planeta():
    def __init__(self):
        self.collection = 'planetas'
        pass

    def add(self, request):
        if not request.json:
            raise InvalidInput('No input data')
        if not ('nome' in request.json and 'clima' in request.json and 'terreno' in request.json):
            raise InvalidInput('Missing some input data')
        if request.json['nome'].strip() == '' or request.json['clima'].strip() == '' or request.json['terreno'].strip() == '':
            raise InvalidInput('Bad input data')

        swapi = SWAPI()
        swapi_planet = swapi.get_planet(request.json['nome'])
        if len(swapi_planet):
            swapi_planet = swapi_planet[0]
        else:
            raise SWAPINotFound('Planet not found in swapi.co')

        planeta = {
            'nome': request.json['nome'],
            'clima': request.json['clima'],
            'terreno': request.json['terreno'],
            'quant_filmes': len(swapi_planet.get('films'))
        }

        mongo.db[self.collection].insert_one(planeta)

        return planeta

    def list(self):
        return mongo.db[self.collection].find()

    def get_by_oid(self, oid):
        return mongo.db[self.collection].find_one({'_id': ObjectId(oid)})

    def get_by_nome(self, request):
        if not request.args:
            raise InvalidInput('No search data')
        if 'search' not in request.args:
            raise InvalidInput('Missing search data')
        if request.args['search'].strip() == '':
            raise InvalidInput('Bad search data')

        return mongo.db[self.collection].find({'nome': request.args['search']})

    def delete(self, oid):
        planeta = mongo.db[self.collection].delete_one({'_id': ObjectId(oid)})
        return planeta.deleted_count
