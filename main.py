import glob
import json
import os
import requests
import sys

API_URL = "https://playerdb.co"

def count_advancements(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return len(data.keys())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def fetch_playername(uuid: str) -> str:
    response = requests.get(f"{API_URL}/api/player/minecraft/{uuid}")
    return response.json()["data"] if response.status_code == 200 else None

def format_data(files: list) -> None:
    for file in files:
        if not file.endswith(".json"):
            continue

        count = count_advancements(file)
        playername = fetch_playername(os.path.basename(file).rsplit('.', 1)[0])["player"]["username"]
        print(f"{playername}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <pattern>")
        sys.exit(1)

    pattern = sys.argv[1]
    files = glob.glob(pattern)
    
    if not files:
        print("No files found matching the pattern.")
        exit(1)
    

    format_data(files)
