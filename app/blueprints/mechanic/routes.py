from flask import request, jsonify, abort
from app.extensions import db
from app.models import Mechanic
from .schemas import mechanic_schema, mechanics_schema
from . import mechanic_bp
from marshmallow import ValidationError

@mechanic_bp.route("/", methods = ['POST'])
def create_mechanic():
    data = request.get_json()
    new_mechanic = mechanic_schema.load(data)
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.jsonify(new_mechanic), 201

@mechanic_bp.route("/", methods = ['GET'])
def get_mechanics():
    all_mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(all_mechanics)

@mechanic_bp.route("/<int:id>", methods = ['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get(id)
    return mechanic_schema.jsonify(mechanic)

@mechanic_bp.route("/<int:id>", methods = ['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get(id)
    if not mechanic:
        abort(404, description = "Mechanic not found.")
    try:
        data = request.get_json()
        updated_mechanic = mechanic_schema.load(data, instance = mechanic, partial = True)
        db.session.commit()
        return mechanic_schema.jsonify(updated_mechanic), 200
    except ValidationError as e:
        return jsonify(e.messages), 400
    
@mechanic_bp.route("/<int:id>", methods = ['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get(id)
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": "Mechanic deleted successfully."}), 200

