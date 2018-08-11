from flask import Blueprint
from flask import request
from bson.json_util import dumps

from b2wswapi.planeta import Planeta

api = Blueprint('api', __name__)

p = Planeta()


@api.route('/planeta', methods=['POST'])
def add_planeta():
    try:
        return dumps(p.add(request)), 201
    except Exception as e:
        raise e


@api.route('/planetas', methods=['GET'])
def list_planetas():
    try:
        lista = [planeta for planeta in p.list()]
        return dumps(lista)
    except Exception as e:
        raise e


@api.route('/planeta/<string:oid>', methods=['GET'])
def get_planeta_by_oid(oid):
    try:
        planeta = p.get_by_oid(oid)
        if planeta is None:
            return '', 404
        return dumps(planeta)
    except Exception as e:
        raise e


@api.route('/planeta/', methods=['GET'])
def get_planeta_by_nome():
    try:
        planeta = p.get_by_nome(request)
        if planeta is None:
            return '', 404
        return dumps(planeta)
    except Exception as e:
        raise e

@api.route('/planeta/<string:oid>', methods=['DELETE'])
def delete_planeta(oid):
    try:
        result = p.delete(oid)
        return dumps({'deleted': result}), 200
    except Exception as e:
        raise e
