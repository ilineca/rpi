from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name' : 'Store1',
        'items' : [
            {
            'name' : 'item1',
            'price' : 10.99
            }
        ]
    }
]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/stores', methods=['GET'])
def get_stores():
    return jsonify(stores)

app.run(port=8080)
