from flask import Flask, jsonify, request


app = Flask(__name__)

equipments = {
    101: {
        "id": 101,
        "name": "Equipment A",
        "type": "FCU",
        "status": "active",
    },
    102: {
        "id": 102,
        "name": "Equipment B",
        "type": "AHU",
        "status": "inactive",
    },
}

# Preserve the original misspelled name for compatibility.
equiments = equipments


@app.get("/")
def index():
    return jsonify({"equipment": list(equipments.values())})


@app.get("/equipment")
def get_equipment():
    return jsonify(list(equipments.values()))


@app.get("/equipment/<int:equipment_id>")
def get_equipment_by_id(equipment_id):
    equipment = equipments.get(equipment_id)
    if equipment is None:
        return jsonify({"error": "Equipment not found"}), 404
    return jsonify(equipment)


if __name__ == "__main__":
    # debug=True enables auto-reload on code changes and detailed error pages
    app.run(debug=True)