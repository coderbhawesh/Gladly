import json
import os

STATE_FILE = "last_import.json"

def get_last_import_time():
    if not os.path.exists(STATE_FILE):
        return "1970-01-01T00:00:00Z"
    with open(STATE_FILE) as f:
        return json.load(f).get("last_import")

def save_last_import_time(timestamp):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_import": timestamp}, f)
