# storage.py
import json
import os

DATA_FILE = "data/quotes.json"

def ensure_data_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({}, f)

def load_quotes():
    ensure_data_file()
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_quotes(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
