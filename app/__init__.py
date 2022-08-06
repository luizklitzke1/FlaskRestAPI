import sys

from flask import Flask, Blueprint
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.comanda.comandaController_v1 import api as home_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint("api", __name__)
app.register_blueprint(blueprint)

authorizations = {
    "bearer": {
        "name": "Authorization",
        "in": "header",
        "type": "apiKey",
        "description": "Insert your JWT Token here!"
    }
}
api = Api(app, title="CRUD de Comandas", version="1.0", description="Restful API com Flask para Suficiencia de Web II", prefix="/api", authorizations=authorizations)

api.add_namespace(home_ns, path="/comandas")