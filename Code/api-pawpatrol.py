from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import pandas as pd
import hashlib
import os

app = Flask(__name__)
api = Api(app)

class Data(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("Wilayah", type=str, required=True)
        self.parser.add_argument("Jumlah", type=int, required=True)
        self.parser.add_argument("Meninggal", type=int, required=True)
        self.parser.add_argument("Hilang", type=int, required=True)
        self.parser.add_argument("Terluka", type=int, required=True)
        self.parser.add_argument("Menderita", type=int, required=True)
        self.parser.add_argument("Mengungsi", type=int, required=True)
        self.parser.add_argument("Rumah", type=int, required=True)
        self.parser.add_argument("Pendidikan", type=int, required=True)
        self.parser.add_argument("Kesehatan", type=int, required=True)
        self.parser.add_argument("Peribadatan", type=int, required=True)
        self.parser.add_argument("Fasum", type=int, required=True)
        self.parser.add_argument("Perkantoran", type=int, required=True)
        self.parser.add_argument("Jembatan", type=int, required=True)
        self.parser.add_argument("Pabrik", type=int, required=True)
        self.parser.add_argument("Kios", type=int, required=True)
        self.parser.add_argument("id", type=int, required=True)
        
        json_dir = 'E:/tugas_koko/Mencari_Kerja/Kerjaan/Data'
        json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

        # load data from each file into a dictionary and store in a list
        self.data_list = []
        for file_name in json_files:
            with open(os.path.join(json_dir, file_name), 'r') as f:
                data = json.load(f)
                self.data_list.append(data)

    def get(self, data_id=None):
        if data_id is None:
            return self.data_list
        else:
            # find the row with the matching ID
            row = [d for d in self.data_list if d["id"] == data_id]
            if len(row) == 0:
                return f"No data with id {data_id} found"
            else:
                return row[0]

    def post(self):
        args = self.parser.parse_args()
        # Concatenate the string values of 'Wilayah', 'Jenis Bencana', and 'Tahun' columns
        id_str = str(args['Wilayah']) + str(args['Jenis Bencana']) + str(args['Tahun'])

        # Generate an MD5 hash of the concatenated string
        id_hash = hashlib.md5(id_str.encode('utf-8')).hexdigest()
        item = {
            "id": id_hash, # generate a unique ID
            "Wilayah": args["Wilayah"],
            "Jumlah": args["Jumlah"],
            "Meninggal": args["Meninggal"],
            "Hilang": args["Hilang"],
            "Terluka": args["Terluka"],
            "Menderita": args["Menderita"],
            "Mengungsi": args["Mengungsi"],
            "Rumah": args["Rumah"],
            "Pendidikan": args["Pendidikan"],
            "Kesehatan": args["Kesehatan"],
            "Peribadatan": args["Peribadatan"],
            "Fasum": args["Fasum"],
            "Perkantoran": args["Perkantoran"],
            "Jembatan": args["Jembatan"],
            "Pabrik": args["Pabrik"],
            "Kios": args["Kios"]
        }
        self.data_list.append(item)
        return item
    
    def put(self, data_id):
        args = self.parser.parse_args()
        item = {
            "id": data_id,
            "Wilayah": args["Wilayah"],
            "Jumlah": args["Jumlah"],
            "Meninggal": args["Meninggal"],
            "Hilang": args["Hilang"],
            "Terluka": args["Terluka"],
            "Menderita": args["Menderita"],
            "Mengungsi": args["Mengungsi"],
            "Rumah": args["Rumah"],
            "Pendidikan": args["Pendidikan"],
            "Kesehatan": args["Kesehatan"],
            "Peribadatan": args["Peribadatan"],
            "Fasum": args["Fasum"],
            "Perkantoran": args["Perkantoran"],
            "Jembatan": args["Jembatan"],
            "Pabrik": args["Pabrik"],
            "Kios": args["Kios"]
        }
        for i in range(len(self.data_list)):
            if self.data_list[i]["id"] == data_id:
                self.data_list[i] = item
                return item, 200
        item["id"] = data_id
        self.data_list.append(item)
        return item, 201
    
api.add_resource(Data, "/data", "/data/<int:data_id>")

if __name__ == "__main__":
    app.run(debug=True)