from flask import Flask
from app.extensions import db, ma, limiter
import os
from app.blueprints.mechanic import mechanic_bp
from app.blueprints.service_ticket import service_ticket_bp
from app.blueprints.customer import customer_bp
from app.blueprints.inventory import inventory_bp

def create_app():
    app = Flask(__name__)
    
    FIXED_SECRET_KEY = "mechanic-shop-development-secret-key-2025-very-long-and-secure-fixed"
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', FIXED_SECRET_KEY)
    
    database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mechanic_shop.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f'mysql+mysqlconnector://root:1234ThumbWar@localhost/Mechanic_Shop')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['RATELIMIT_STORAGE_URL'] = 'memory://'
    app.config['RATELIMIT_DEFAULT'] = "1000 per hour"
    
    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
        
    app.register_blueprint(mechanic_bp, url_prefix = '/mechanics')
    app.register_blueprint(service_ticket_bp, url_prefix = '/service-tickets')
    app.register_blueprint(customer_bp, url_prefix = '/customers')
    app.register_blueprint(inventory_bp, url_prefix = '/inventory')
    
    @app.route('/')
    def home():
        return {
            'message': 'Mechanic Shop API',
            'version': '1.0',
            'status': 'running',
            'database': 'SQLite',
            'endpoints': {
                'mechanics': '/mechanics/',
                'customers': '/customers/', 
                'service_tickets': '/service-tickets/',
                'inventory': '/inventory/'
            }
        }
    
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'database': 'connected', 'type': 'SQLite'}
    
    return app