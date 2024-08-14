from flask import Blueprint, jsonify
from .utils import fetch_data, process_data, store_data, get_processed_data

api = Blueprint("api", __name__)


@api.route("/fetch-data", methods=["GET"])
def fetch_data_endpoint():
    data = fetch_data()
    processed_data = process_data(data)
    store_data(processed_data)
    return jsonify({"message": "Data fetched and processed successfully"}), 200


@api.route("/get-processed-data", methods=["GET"])
def get_processed_data_endpoint():
    data = get_processed_data()
    return jsonify({"data": data, "success": True}), 200
import random

# In-memory storage for processed data
in_memory_store = []

def fetch_data(num_entries=1000):
    # Simulate fetching a large dataset
    data = []
    for i in range(1, num_entries + 1):
        order = {
            "order_id": i,
            "apple": random.randint(1, 100),
            "banana": random.randint(1, 100),
            "currency": "USD"
        }
        data.append(order)
    return data

def process_data(data):
    # Process data by adding a new key 'total' which is the sum of apple and banana
    processed_data = []
    for entry in data:
        processed_entry = {
            "order_id": entry["order_id"],
            "apple": entry["apple"],
            "banana": entry["banana"],
            "currency": entry["currency"],
            "total": entry["apple"] + entry["banana"]
        }
        processed_data.append(processed_entry)
    return processed_data

def store_data(data):
    # Store the processed data in memory
    global in_memory_store
    in_memory_store = data

def get_processed_data():
    # Retrieve the processed data from memory
    return in_memory_store
