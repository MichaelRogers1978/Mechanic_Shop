from app import create_app
from app.extensions import db
from app.models import Mechanic, Admin, Customer
from werkzeug.security import generate_password_hash
from flask_swagger_ui import get_swaggerui_blueprint
import os
from jose import jwt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

app = create_app("testing")

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {'app_name': "Mehaninc Shop"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix = SWAGGER_URL)

#if __name__ == "__main__":
    #with app.app_context():
        #print("Initializing Mechanic Shop Database.")
        
        #db.drop_all()>
        
        #db.create_all()
        #print("Database tables ready!")
        
       # from app.autho.utils import get_secret_key
        #secret_key = get_secret_key()
        #print(f"Secret key configured: {bool(app.config.get('SECRET_KEY'))}")
       # print(f"Secret key length: {len(secret_key)}")
       # print(f"Secret key preview: {secret_key[:20]}.")
       # print(f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')}")
        
       # from app.autho.utils import encode_mechanic_token
       # print(f"Testing JWT with secret key: {secret_key[:20]}.")
       # test_token = encode_mechanic_token(999)
       # if test_token:
            #print(f"JWT encoding test successful (token length: {len(test_token)})")
            
           # try:
            #    decoded = jwt.decode(test_token, secret_key, algorithms = ["HS256"])
            #    print(f"JWT decode test successful: {decoded}")
            #except Exception as decode_error:
                #print(f"JWT decode test failed: {decode_error}")
        #else:
           # print("JWT encoding test failed!")
            
        #print("\n" + "=" *50)
        #print("ADMIN SETUP COMPLETE")
        #print("=" *50)
        #print("Admin Login Credentials:")
        #print("  Username: admin")
       # print("  Password: admin123") 
        #print("  Login URL: POST /mechanics/admin/login")
       # print("=" *50)
        
       # print("=" *50 + "\n")
        
   # print("Starting Flask application...")
    #print("Tokens will be valid for 8 hours")
    #print("API available at: http://localhost:5000")
    #print(f"Using secret key: {get_secret_key()[:20]}.")