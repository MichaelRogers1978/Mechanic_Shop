from flask import request, jsonify
from app.extensions import db
from app.models import ServiceTicket, Mechanic
from . import service_ticket_bp
from .schemas import ticket_schema, tickets_schema

@service_ticket_bp.route("/", methods = ['POST'])
def create_ticket():
    data = request.get_json()
    ticket = ticket_schema.load(data)
    db.session.add(ticket)
    db.session.commit()
    return ticket_schema.jsonify(ticket), 201

@service_ticket_bp.route("/", methods = ['GET'])
def get_tickets():
    tickets = ServiceTicket.query.all()
    return tickets_schema.jsonify(tickets)

@service_ticket_bp.route("/<int:ticket_id>/assign-mechanic/<int:mechanic_id>", methods = ['PUT'])
def assign_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    
    if mechanic not in ticket.mechanics:
        ticket.mechanics.append(mechanic)
        db.session.commit()
        
    return ticket_schema.jsonify(ticket)

@service_ticket_bp.route("/<int:ticket_id>/remove-mechanic/<int:mechanic_id>", methods = ['PUT'])
def remove_mechanic(ticket_id, mechanic_id):
    ticket = ServiceTicket.query.get_or_404(ticket_id)
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    
    if mechanic in ticket.mechanics:
        ticket.mechanics.remove(mechanic)
        db.session.commit()
        
    return ticket_schema.jsonify(ticket)