import pytest
from flask import jsonify
from flask.json import loads
from bson.json_util import dumps

from b2wswapi import create_app

object_id = None
nome = 'Tatooine'

@pytest.fixture
def app():
    config = {
        'MONGO_URI': 'mongodb://localhost:27017/b2wswapi',
        'BASE_URL': '/b2wswapi/api/v1.0',
        'TESTING': True
    }
    client = create_app(config)

    yield client


@pytest.fixture
def client(app):
    return app.test_client()


def test_add_error_nome(client, app):
    nome = ''
    clima = 'árido'
    terreno = 'deserto'

    with app.app_context():
        response = loads(client.post(
            '/b2wswapi/api/v1.0/planeta',
            data=dumps({
                'nome': nome,
                'clima': clima,
                'terreno': terreno
            }),
            content_type='application/json'
        ).data)

    assert 'Bad input data' == response['message']


def test_add_error_clima(client, app):
    global nome
    clima = ''
    terreno = 'deserto'

    with app.app_context():
        response = loads(client.post(
            '/b2wswapi/api/v1.0/planeta',
            data=dumps({
                'nome': nome,
                'clima': clima,
                'terreno': terreno
            }),
            content_type='application/json'
        ).data)

    assert 'Bad input data' == response['message']


def test_add_error_terreno(client, app):
    global nome
    clima = 'árido'
    terreno = ''

    with app.app_context():
        response = loads(client.post(
            '/b2wswapi/api/v1.0/planeta',
            data=dumps({
                'nome': nome,
                'clima': clima,
                'terreno': terreno
            }),
            content_type='application/json'
        ).data)

    assert 'Bad input data' == response['message']


def test_add_error_swapi(client, app):
    nome = 'PlanetNotFoundInSWAPI'
    clima = 'árido'
    terreno = 'deserto'

    with app.app_context():
        response = loads(client.post(
            '/b2wswapi/api/v1.0/planeta',
            data=dumps({
                'nome': nome,
                'clima': clima,
                'terreno': terreno
            }),
            content_type='application/json'
        ).data)

    assert 'Planet not found in swapi.co' == response['message']


def test_add(client, app):
    global object_id
    global nome
    clima = 'árido'
    terreno = 'deserto'

    with app.app_context():
        response = loads(client.post(
            '/b2wswapi/api/v1.0/planeta',
            data=dumps({
                'nome': nome,
                'clima': clima,
                'terreno': terreno
            }),
            content_type='application/json'
        ).data)

    object_id = response['_id']['$oid']

    assert (nome == response['nome'] and
        clima == response['clima'] and
        terreno == response['terreno'] and
        'quant_filmes' in response)


def test_list(client):
    global nome

    response = loads(client.get('/b2wswapi/api/v1.0/planetas').data)

    assert type(response) == list
    assert nome == response[0]['nome']


def test_get_by_id(client, app):
    global object_id
    global nome

    with app.app_context():
        response = loads(client.get(
            '/b2wswapi/api/v1.0/planeta/' + object_id
        ).data)

    assert nome == response['nome']


def test_get_by_nome(client, app):
    global nome

    with app.app_context():
        response = loads(client.get(
            '/b2wswapi/api/v1.0/planeta/?search=' + nome
        ).data)

    assert type(response) == list
    assert nome == response[0]['nome']


def test_delete(client, app):
    global object_id

    with app.app_context():
        response = loads(client.delete(
            '/b2wswapi/api/v1.0/planeta/' + object_id
        ).data)

    assert 1 == response['deleted']
