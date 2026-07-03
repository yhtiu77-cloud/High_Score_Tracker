# 🏆 High Score Tracker

A simple command-line high score tracker that saves and loads scores from a JSON file.

## Setup

```bash
# No dependencies — uses the Python standard library only
python main.py
```

## Usage

| Option | Action |
|---|---|
| `1` | Add a new player and score |
| `2` | Update an existing player's score |
| `3` | View the leaderboard |
| `4` | Quit |

Scores are saved to `highscore.json` automatically after every change.

## What I Learned

- Reading and writing JSON files with Python's `json` module
- Using `try/except` for file handling and input validation
- Storing structured data as a list of dictionaries
- Sorting a list of dictionaries by a key with `sorted()` and `lambda`

## License

MIT
