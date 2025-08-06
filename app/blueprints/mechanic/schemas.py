from app.extensions import ma
from app.models import Mechanic, ServiceTicket

class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        load_instance = True
        
class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        load_instance = True
        
mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many = True)
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many = True)