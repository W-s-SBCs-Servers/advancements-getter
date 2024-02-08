import glob
import os
import subprocess
import sys

def update_scoreboard(files: list, screen: str, score: str) -> None:
    for file in files:
        if not os.path.exists(file):
            raise FileNotFoundError(f"File '{file}' not found.")

        with open(file, 'r') as f:
            for line in f.readlines():
                player, value, _ = line.split(' ')
                command_to_run = f"scoreboard players set {player} {score} {value}"
                subprocess.run(["screen", "-S", screen, "-X", "stuff", f"{command_to_run}\n"])


if __name__ == "__main__":
    if os.name != 'posix':
        print('This script was designed for Linux.')
        exit(1)

    if len(sys.argv) != 4:
        print("Usage: python3 main.py <pattern> <server_screen_name> <minecraft_score_name>")
        exit(1)

    pattern = sys.argv[1]
    files = glob.glob(pattern)

    if not files:
        print("No files found matching the pattern.")
        exit(1)

    update_scoreboard(files, sys.argv[2], sys.argv[3])
