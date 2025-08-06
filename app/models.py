from .extensions import db

ticket_mechanic = db.Table('ticket_mechanic',
    db.Column('service_ticket_id', db.Integer, db.ForeignKey('service_ticket.id'), primary_key = True),
    db.Column('mechanic_id', db.Integer, db.ForeignKey('mechanic.id'), primary_key = True)
)

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(300), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    address = db.Column(db.String(200), nullable = False)
    hours_worked = db.Column(db.Integer, nullable = False)
    
class ServiceTicket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer_id = db.Column(db.Integer, nullable = False)
    vehicle_id = db.Column(db.String(200), nullable = False)
    hours_worked = db.Column(db.Integer, nullable = False)
    repair = db.Column(db.String(500), nullable = False)
    
    
    mechanics = db.relationship('Mechanic', secondary = ticket_mechanic, backref = 'service_tickets')
    
    