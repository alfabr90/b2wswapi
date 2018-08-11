from flask import Blueprint
from flask import jsonify

from b2wswapi.exceptions.invalid_input import InvalidInput
from b2wswapi.exceptions.swapi_notfound import SWAPINotFound

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(Exception)
def handle_error(e):
    return jsonify({'message': str(e)}), 500


@errors.app_errorhandler(InvalidInput)
@errors.app_errorhandler(SWAPINotFound)
def handle_invalid_input(e):
    return jsonify(e.to_dict()), e.status_code
