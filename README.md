# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/). This is a work in progress from boot.dev's "Build a Video Game with Python" course.

## Status

🚧 Early stage — currently just initializes pygame and opens the game window. Gameplay (player ship, movement, asteroids, shooting, collisions) is not implemented yet.

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

- `main.py` — entry point, sets up the pygame window
- `constants.py` — game constants (screen size, etc.)
