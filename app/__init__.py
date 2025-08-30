from flask import Flask, jsonify
from app.extensions import db, ma, limiter
from app.blueprints.mechanic import mechanic_bp
from app.blueprints.service_ticket import service_ticket_bp
from app.blueprints.customer import customer_bp
from app.blueprints.inventory import inventory_bp
from flask_swagger_ui import get_swaggerui_blueprint
from app.config import config
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

def create_app(config_name=None):
    config_name = config_name or 'development'

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from . import models

    app.register_blueprint(mechanic_bp, url_prefix='/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix='/service-tickets')
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    @app.route('/')
    def home():
        return {
            'message': 'Mechanic Shop API',
            'version': '1.0',
            'status': 'running',
            'endpoints': {
                'mechanics': '/mechanics/',
                'customers': '/customers/',
                'service_tickets': '/service-tickets/',
                'inventory': '/inventory/'
            }
        }

    @app.route('/health')
    def health():
        return {'status': 'healthy'}

    return app