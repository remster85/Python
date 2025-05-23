import time
import json
import hashlib
import os
from datetime import datetime

POLL_INTERVAL = 10  # seconds
SAVE_DIR = "history"
LAST_DIR = "last"

os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(LAST_DIR, exist_ok=True)


def compute_hash(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()


def load_last_data(name):
    path = os.path.join(LAST_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None


def update_last_data(name, data):
    path = os.path.join(LAST_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def save_versioned_data(name, data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(SAVE_DIR, f"{name}_{timestamp}.json")
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ [{name}] New version saved: {filename}")


def monitor(name, fetch_func):
    last_data = load_last_data(name)
    last_hash = compute_hash(last_data) if last_data else None

    try:
        current_data = fetch_func()
        if current_data is None:
            print(f"⚠️  [{name}] No data fetched.")
            return

        current_hash = compute_hash(current_data)
        if current_hash != last_hash:
            save_versioned_data(name, current_data)
            update_last_data(name, current_data)
        else:
            print(f"✅ [{name}] No changes.")
    except Exception as e:
        print(f"❌ [{name}] Error: {e}")


# ✍️ Define your fetch functions here
import requests

def fetch_iss_position():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    return response.json()

def fetch_ip():
    response = requests.get("https://api.ipify.org?format=json")
    return response.json()


# 🧠 Registry of tasks to monitor
MONITOR_TASKS = {
    "iss_position": fetch_iss_position,
    "public_ip": fetch_ip,
    # Add more: "task_name": fetch_function
}


def main():
    while True:
        for name, func in MONITOR_TASKS.items():
            monitor(name, func)
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
