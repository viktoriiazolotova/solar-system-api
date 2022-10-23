from flask import Blueprint, jsonify
class Planet():
    def __init__(self, id, name, decsription, color):
        self.id = id
        self.name = name
        self.decsription = decsription
        self.color = color

planet_items = [
    Planet(1, "Mars", "the forth planet by size", "red"),
    Planet(2, "Venus", "the second planet by size", "yellow"),
    Planet(3, "Mercury", "the smallest by the size", "grey")
]

planet_bp = Blueprint("planets", __name__, url_prefix = "/planets")
@planet_bp.route("", methods = ["GET"])

def get_all_planets():
    result = []
    for planet in planet_items:
        planet_dict = {"id": planet.id,
                        "name": planet.name,
                        "description": planet.decsription,
                        "color": planet.color}
        result.append(planet_dict)
    return jsonify(result), 200

#WAVE TWO 

@planet_bp.route("/<planet_id>", methods = ["GET"])

def get_one_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return jsonify({"msg":f'Invalid data type: {planet_id}'}), 400
    choosing_planet = None 
    for planet in planet_items:
        if planet.id == planet_id:
            choosing_planet = planet 
    if choosing_planet is None: 
        return jsonify({"msg":f'Can not find planet id {planet_id}'}), 404

    choosing_planet = {"id": choosing_planet.id,
                        "name": choosing_planet.name,
                        "description": choosing_planet.decsription,
                        "color": choosing_planet.color}
    return jsonify(choosing_planet), 200