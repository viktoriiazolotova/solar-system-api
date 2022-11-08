import re
from flask import Blueprint, jsonify, make_response, request, abort
from app.models.planet import Planet
from app import db 



planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planet_bp.route("", methods=['POST'])
def create_one_planet():
    request_body = request.get_json()
    new_planet = Planet(name= request_body["name"],
                        description= request_body["description"],
                        color = request_body["color"])
    db.session.add(new_planet)
    db.session.commit()
    return make_response(f"Planet {new_planet.name} successfully created with id {new_planet.id}."), 201



@planet_bp.route("", methods = ['GET'])
def get_all_planets():
    name_query_value = request.args.get('name')
    result = []
    if name_query_value:
        all_planet = Planet.query.filter_by(name = name_query_value)
    else: 
        all_planet = Planet.query.all()
        
    for planet in all_planet:
        result.append(planet.to_dict())
    return jsonify(result), 200

@planet_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    choosen_planet = get_planet_from_id(planet_id)
    return jsonify(choosen_planet.to_dict()), 200

@planet_bp.route("<planet_id>", methods = ['PUT'])
def update_one_planet(planet_id):
    update_planet = get_planet_from_id(planet_id)
    request_body = request.get_json()
    try:
        update_planet.name = request_body["name"]
        update_planet.description = request_body["description"]
        update_planet.color = request_body["color"]
    except KeyError:
        # if request_body["color"] is None:
        #     return jsonify({"msg": "Missing needed color input"}), 400
        return jsonify({"msg": "Missing needed data"}), 400
    db.session.commit()
    return jsonify({"msg": f"Successfully updated planet with id {update_planet.id}"}), 200

@planet_bp.route("<planet_id>", methods = ['DELETE'])
def delete_one_planet(planet_id):
    delete_planet = get_planet_from_id(planet_id)
    db.session.delete(delete_planet)
    db.session.commit()
    return jsonify({"msg": f"Successfully deleted one planet with id {delete_planet.id}"}), 200

def get_planet_from_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({"msg":f'Invalid data type: {planet_id}'}, 400))

    choosen_planet = Planet.query.get(planet_id)

    if choosen_planet is None:
        return abort(make_response({"msg": f"Can not find planet id {planet_id}"}, 404
 ))
    return choosen_planet



