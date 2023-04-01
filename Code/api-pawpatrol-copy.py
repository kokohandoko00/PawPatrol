from flask import Flask, jsonify, request
import json
import pandas as pd
import hashlib
import os

app = Flask(__name__)

json_dir = 'E:/tugas_koko/Mencari_Kerja/Kerjaan/Paw_Patrol/Development/Data'
json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

# load data from each file into a dictionary and store in a list
data_list = []
for file_name in json_files:
    with open(os.path.join(json_dir, file_name), 'r') as f:
        data = json.load(f)
        data_list.append(data)

@app.route('/')
def index():
    return 'Welcome to the Patron API!'

@app.route('/data', methods=['GET'])
def get_all():
    return jsonify(data_list)

@app.route('/data/<int:data_id>', methods=['GET'])
def get(data_id=None):
    row = [d for d in data_list if d["id"] == data_id]
    if len(row) == 0:
        return f"No data with id {data_id} found"
    else:
        return row[0]

@app.route('/data', methods=['POST'])
def post():

    # Extract the JSON payload from the request body
    data = request.get_json()
   
   # Validate that the required attributes are present in the JSON payload
    required_attributes = ['Wilayah', 'Jumlah', 'Meninggal', 'Hilang', 'Terluka', 'Menderita', 'Mengungsi', 'Rumah', 'Pendidikan', 'Kesehatan', 'Peribadatan', 'Fasum', 'Perkantoran', 'Jembatan', 'Pabrik', 'Kios']
    for attr in required_attributes:
        if attr not in data:
            return jsonify({'error': f'Missing required attribute: {attr}'}), 400
    # Concatenate the string values of 'Wilayah', 'Jenis Bencana', and 'Tahun' columns
    id_str = str(data['Wilayah']) + str(data['Jenis Bencana']) + str(data['Tahun'])

    # Generate an MD5 hash of the concatenated string
    id_hash = hashlib.md5(id_str.encode('utf-8')).hexdigest()
    item = {
        "id": id_hash, # generate a unique ID
        "Wilayah": data["Wilayah"],
        "Jumlah": data["Jumlah"],
        "Meninggal": data["Meninggal"],
        "Hilang": data["Hilang"],
        "Terluka": data["Terluka"],
        "Menderita": data["Menderita"],
        "Mengungsi": data["Mengungsi"],
        "Rumah": data["Rumah"],
        "Pendidikan": data["Pendidikan"],
        "Kesehatan": data["Kesehatan"],
        "Peribadatan": data["Peribadatan"],
        "Fasum": data["Fasum"],
        "Perkantoran": data["Perkantoran"],
        "Jembatan": data["Jembatan"],
        "Pabrik": data["Pabrik"],
        "Kios": data["Kios"]
        }
    data_list.append(item)
    return item

@app.route('/data/<int:data_id>', methods=['PUT'])    
def put(data_id):
    data = request.json
    item = {
        "id": data_id,
        "Wilayah": data["Wilayah"],
        "Jumlah": data["Jumlah"],
        "Meninggal": data["Meninggal"],
        "Hilang": data["Hilang"],
        "Terluka": data["Terluka"],
        "Menderita": data["Menderita"],
        "Mengungsi": data["Mengungsi"],
        "Rumah": data["Rumah"],
        "Pendidikan": data["Pendidikan"],
        "Kesehatan": data["Kesehatan"],
        "Peribadatan": data["Peribadatan"],
        "Fasum": data["Fasum"],
        "Perkantoran": data["Perkantoran"],
        "Jembatan": data["Jembatan"],
        "Pabrik": data["Pabrik"],
        "Kios": data["Kios"]
    }
    for i in range(len(data_list)):
        if data_list[i]["id"] == data_id:
            data_list[i] = item
            return item, 200
    item["id"] = data_id
    data_list.append(item)
    return item, 201

@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete(data_id):
    for i in range(len(data_list)):
        if data_list[i]['id'] == data_id:
            del data_list[i]
            return '', 204
    return {'message': 'Data not found'}, 404


if __name__ == "__main__":
    app.run(debug=True)