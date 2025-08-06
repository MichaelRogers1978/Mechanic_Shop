from flask import Flask
from .config import Config
from .extensions import db, ma
from .blueprints.mechanic import mechanic_bp
from .blueprints.service_ticket import service_ticket_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(service_ticket_bp)
    
    db.init_app(app)
    ma.init_app(app)
    
    app.register_blueprint(mechanic_bp)
    
    with app.app_context():
        db.create_all()
    
    return app