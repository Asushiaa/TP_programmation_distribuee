
from flask import Flask, jsonify, request

from service.cat_service import CatService

app = Flask(__name__)

cat_service = CatService()


# Vérifier que le service fonctionne
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"message": "Cats service is running"}), 200


# Récupérer les chats disponibles
@app.route("/cats", methods=["GET"])
def get_cats():
    cats = cat_service.get_all_cats()
    available_cats = [
        cat for cat in cats
        if cat["status"] == "available"
    ]
    return jsonify(available_cats), 200


# Récupérer un chat par son identifiant
@app.route("/cats/<int:cat_id>", methods=["GET"])
def get_cat(cat_id):
    cat = cat_service.get_cat_by_id(cat_id)

    if cat is None:
        return jsonify({"message": "Cat not found"}), 404

    return jsonify(cat), 200


# Adopter ou rendre disponible un chat
@app.route("/cats/<int:cat_id>", methods=["PUT"])
def adopt_or_release_cat(cat_id):
    cat = cat_service.get_cat_by_id(cat_id)

    if cat is None:
        return jsonify({"message": "Cat not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"message": "A JSON object is required"}), 400

    action = data.get("action")

    if action == "adopt":
        if cat["status"] == "adopted":
            return jsonify({"message": "Cat is already adopted"}), 400

        cat_service.update_cat_status(cat_id, "adopted")
        return jsonify({"message": "Cat adopted successfully"}), 200

    if action == "release":
        if cat["status"] == "available":
            return jsonify({"message": "Cat is already available"}), 400

        cat_service.update_cat_status(cat_id, "available")
        return jsonify({"message": "Cat is available again"}), 200

    return jsonify({
        "message": "action must be adopt or release"
    }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)