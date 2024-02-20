import glob
import json
import os
import requests
import sys

API_URL = "https://playerdb.co"
USER_AGENT = "W-s-SBCs-Servers/advancements-getter (GitHub: https://github.com/W-s-SBCs-Servers/advancements-getter)"

def count_advancements(filename: str) -> int:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    with open(filename, 'r') as file:
        data = json.load(file)
        return sum(1 for advancement in data.values() if isinstance(advancement, dict) and advancement.get('done'))

def fetch_playername(uuid: str) -> dict:
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(f"{API_URL}/api/player/minecraft/{uuid}", headers=headers)
    return response.json()["data"] if response.status_code == 200 else None

def format_data(files: list) -> None:
    for file in files:
        if not file.endswith(".json"):
            continue

        count = count_advancements(file)
        player_data = fetch_playername(os.path.basename(file).rsplit('.', 1)[0])

        if player_data:
            playername = player_data["player"]["username"]
            print(f"{playername} {count}")

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
    
