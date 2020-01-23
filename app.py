import os

from flask import Flask

from flask_log_request_id import RequestID, RequestIDLogFilter
import logging

req_id = RequestID()


def setup_blueprints(app):
    from blueprints import simple_blueprint

    app.register_blueprint(simple_blueprint)


def setup_logging():
    handler = logging.StreamHandler()
    logging.getLogger("werkzeug").handlers = []
    handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - request_id=%(request_id)s - %(message)s"))
    handler.addFilter(RequestIDLogFilter())
    logging.getLogger().addHandler(handler)

def create_app():
    app = Flask(__name__)

    setup_blueprints(app)

    setup_logging()
    req_id.init_app(app)

    return app
