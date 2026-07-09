# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/). This is a work in progress from boot.dev's "Build a Video Game with Python" course.

## Status

Early stage — pygame is initialized and opens the game window, running a basic game loop (event handling, black screen clear/flip, delta-time clock capped at 60 FPS) plus periodic game state logging. Gameplay (player ship, movement, asteroids, shooting, collisions) is not implemented yet.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Setup

```bash
uv sync
```

## Running

```bash
uv run main.py
```

## Project structure

- `main.py` — entry point; sets up the pygame window and runs the main game loop
- `constants.py` — game constants (screen size, etc.)
- `logger.py` — writes periodic game state (`game_state.jsonl`) and event (`game_events.jsonl`) snapshots for debugging
