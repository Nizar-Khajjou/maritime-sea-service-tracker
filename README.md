# ⚓ Maritime Sea-Service Day Tracker

A Python tool that tracks and visualizes sea-service training days using the Pixela API — built to log progress toward STCW maritime qualification requirements.

## What it does
- Creates a Pixela user account via REST API
- Creates a custom graph to track daily sea-service logging
- Posts daily pixel data (1 day logged = 1 pixel)
- Generates a visual heatmap graph of progress over time

## Why this project
As a maritime professional working toward my official Patrón de Altura qualification, I need to track sea-service days. This tool turns that requirement into a visual, motivating habit tracker.

## Built with
- Python 3
- requests library
- Pixela API (graph visualization service)
- python-dotenv (secure token management)

## Security
API tokens are stored in a `.env` file (excluded from version control via `.gitignore`) and loaded securely using environment variables — never hardcoded in the source code.

## How to use
1. Clone the repo
2. Create a `.env` file with your own `PIXELA_TOKEN`
3. Run `main.py` to create your user, graph, and log your first day

## Author
Nizar Khajjou — Maritime Professional | Data Science in Progress
🔗 [LinkedIn](https://linkedin.com/in/nizar-khajjou-47b67b3b2)
🔗 [GitHub](https://github.com/Nizar-Khajjou)
