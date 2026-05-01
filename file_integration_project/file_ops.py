import os
import json
from datetime import datetime

HASH_FILE = "hash_store.json"
LOG_FILE = "log.txt"

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    return {}

def save_hash(file_path, hash_value):
    hashes = load_hashes()
    hashes[file_path] = hash_value

    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

def update_hash(file_path, new_hash):
    hashes = load_hashes()
    hashes[file_path] = new_hash

    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)

def log_event(message):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {message}\n")