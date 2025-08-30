import unittest
from app import create_app, db
from app.models import Customer, Mechanic
from werkzeug.security import generate_password_hash
from app.autho.utils import encode_customer_token, encode_admin_token, encode_mechanic_token

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            
            print("Tables after creat_all():", db.inspect(db.engin).get_table_names())

            self.admin_email = "admin@example.com"
            self.admin_password = "adminpass"
            self.admin = Customer(
                name = "Admin User",
                email = self.admin_email,
                phone = 1111111111,
                password = generate_password_hash(self.admin_password)
            )
            db.session.add(self.admin)
            db.session.commit()

            self.customer_email = "cust@example.com"
            self.customer_password = "custpass123"
            self.customer = Customer(
                name = "Jane Doe",
                email = self.customer_email,
                phone = 2222222222,
                password = generate_password_hash(self.customer_password)
            )
            db.session.add(self.customer)
            db.session.commit()

            self.mech_email = "mech@example.com"
            self.mech_password = "mechpass123"
            self.mechanic = Mechanic(
                name = "Bob Mechanic",
                email = self.mech_email,
                phone = 3333333333,
                password = generate_password_hash(self.mech_password)
            )
            db.session.add(self.mechanic)
            db.session.commit()

            self.admin_token = encode_admin_token(self.admin.id)
            self.customer_token = encode_customer_token(self.customer.id)
            self.mechanic_token = encode_mechanic_token(self.mechanic.id)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def auth_header(self, token):
        return {"Authorization": f"Bearer {token}"}
