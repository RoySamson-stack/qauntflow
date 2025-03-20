from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the QuantFlow App!"})

@app.route('/items', methods=['GET'])
def get_items():
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = {"id": item_id, "name": f"Item {item_id}"}
    return jsonify(item)

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {"id": 3, "name": data.get("name")}
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    updated_item = {"id": item_id, "name": data.get("name")}
    return jsonify(updated_item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify({"message": f"Item {item_id} deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)