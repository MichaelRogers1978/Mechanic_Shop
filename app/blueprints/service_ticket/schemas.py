from app.extensions import ma
from app.models import ServiceTicket
from app.blueprints.mechanic.schemas import MechanicSchema

class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTicket
        include_fk = True
        load_instance = True
        
    mechanics = ma.Nested(MechanicSchema, many = True)
    
ticket_schema = ServiceTicketSchema()
tickets_schema = ServiceTicketSchema(many = True)