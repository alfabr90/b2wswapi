import os

from flask import Flask

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    if config is None:
        app.config.from_pyfile(os.environ['CONFIG_FILE'])
    else:
        app.config.from_mapping(config)

    from b2wswapi.planeta import mongo
    mongo.init_app(app)

    from b2wswapi.api import api
    app.register_blueprint(api, url_prefix=app.config['BASE_URL'])
    from b2wswapi.errors import errors
    app.register_blueprint(errors)

    return app
