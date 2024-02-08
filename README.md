# Minecraft Advancements Getter

This repository contains two Python scripts for retrieving players' advancements in a Minecraft world and displaying or updating them in-game using a scoreboard.

## Features

### main.py

- `main.py` retrieves players' advancements from JSON files and displays players' names along with the number of advancements achieved.

### scoreboard.py

- `scoreboard.py` updates players' scores in the game based on their progress in Minecraft advancements.

## Prerequisites

- Python 3.x
- The `requests` library

## Installing Dependencies

Dependencies can be installed by running the following command in the terminal:

```bash
pip install -r requirements.txt
```

## Recommended Usage

### For `main.py`:

```bash
python3 main.py "path/to/advancements/*.json" > output.txt
```

### For `scoreboard.py`:

```bash
python3 scoreboard.py "input_files.txt" server_screen_name minecraft_score_name
```

## Contributions

Contributions are welcome. Please provide clear and concise explanations of your contributions in your Pull Requests.

## Notes

- The `scoreboard.py` script is currently designed to work only on Linux.
