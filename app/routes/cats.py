import json
from flask import Blueprint, jsonify

class Cat:
    def __init__(self, id, name, age, color):
        self.id = id
        self.name = name
        self.age = age
        self.color = color

cats = [
    Cat(1, "Nero", 6, "black"),
    Cat(2, "Cid", 7, "white"), 
    Cat(3, "Biggs", 7, "blue"),
    Cat(4, "Wedge", 5, "brown")
    ]

cats_bp = Blueprint("cats", __name__, url_prefix="/cats")

@cats_bp.route("/cats", methods=["GET"])
def get_all_cats():
    cat_response = []
    for cat in cats:
        cat_response.append({
            "id": cat.id,
            "name": cat.name,
            "age": cat.age,
            "color": cat.color
        })
    return jsonify(cat_response)

@cats_bp.route("/<cat_id>", methods=["GET"])
def get_one_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        rsp = {"msg": f"Invalid ID: {cat_id}"}   
        return jsonify(rsp), 400
    chosen_cat = None
    for cat in cats:
        if cat.id == cat_id:
            chosen_cat = cat
            break
    if chosen_cat is None:
        rsp = {"msg": f"We could not find a cat with id {cat_id}"}
        return jsonify(rsp), 404
    rsp = {
        "id": chosen_cat.id,
        "name": chosen_cat.name,
        "age": chosen_cat.age,
        "color": chosen_cat.color
    }        

    return jsonify(rsp), 200


