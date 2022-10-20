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