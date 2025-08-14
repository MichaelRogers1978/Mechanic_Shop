from app import create_app
from app.extensions import db
from app.models import Mechanic
from werkzeug.security import generate_password_hash

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        print("Initializing Mechanic Shop Database.")
        
        #db.drop_all()
        
        db.create_all()
        print("Database tables ready!")
        
        from app.autho.utils import get_secret_key
        secret_key = get_secret_key()
        print(f"Secret key configured: {bool(app.config.get('SECRET_KEY'))}")
        print(f"Secret key length: {len(secret_key)}")
        print(f"Secret key preview: {secret_key[:20]}.")
        print(f"Database URI: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')}")
        
        from app.autho.utils import encode_mechanic_token
        print(f"Testing JWT with secret key: {secret_key[:20]}.")
        test_token = encode_mechanic_token(999)
        if test_token:
            print(f"JWT encoding test successful (token length: {len(test_token)})")
            
            from jose import jwt
            try:
                decoded = jwt.decode(test_token, secret_key, algorithms = ["HS256"])
                print(f"JWT decode test successful: {decoded}")
            except Exception as decode_error:
                print(f"JWT decode test failed: {decode_error}")
        else:
            print("JWT encoding test failed!")
        
        try:
            test_mechanic = Mechanic.query.filter_by(email = "test@mechanic.com").first()
            if not test_mechanic:
                test_mechanic = Mechanic(
                    name = "Test Mechanic",
                    email = "test@mechanic.com",
                    phone = "1234567890",
                    address = "123 Test St",
                    hours_worked = 0,
                    password = generate_password_hash("test123")
                )
                db.session.add(test_mechanic)
                db.session.commit()
                print("Test mechanic created: test@mechanic.com / test123")
            else:
                print("Test mechanic already exists: test@mechanic.com / test123")
                
        except Exception as e:
            print(f"Test data creation failed: {e}")
            db.session.rollback()
        
        try:
            from app.models import Customer
            test_customer = Customer.query.filter_by(email="test@customer.com").first()
            if not test_customer:
                test_customer = Customer(
                    name = "Test Customer",
                    email = "test@customer.com",
                    phone = 9876543210,
                    address = "456 Customer Ave",
                    password = generate_password_hash("customer123")
                )
                db.session.add(test_customer)
                db.session.commit()
                print("Test customer created: test@customer.com / customer123")
            else:
                print("Test customer already exists: test@customer.com / customer123")
                
        except Exception as e:
            print(f"Test customer creation failed: {e}")
            db.session.rollback()
            
        print("\n" + "=" *50)
        print("ADMIN SETUP COMPLETE")
        print("=" *50)
        print("Admin Login Credentials:")
        print("  Username: admin")
        print("  Password: admin123") 
        print("  Login URL: POST /mechanics/admin/login")
        print("=" *50)
        
        try:
            from app.autho.utils import encode_admin_token
            test_admin_token = encode_admin_token(1)
            if test_admin_token:
                print(f"Admin token test successful (length: {len(test_admin_token)})")
                print(f"   Token preview: {test_admin_token[:30]}.")
            else:
                print("Admin token test failed!")
        except ImportError:
            print("encode_admin_token not found - add to app/autho/utils.py")
        except Exception as admin_error:
            print(f"Admin token test error: {admin_error}")
        
        print("=" *50 + "\n")
        
    print("Starting Flask application...")
    print("Tokens will be valid for 8 hours")
    print("API available at: http://localhost:5000")
    print(f"Using secret key: {get_secret_key()[:20]}.")
    app.run(debug = True, host = '0.0.0.0', port = 5000)