# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/)

## Status

Early stage — pygame is initialized and opens the game window, running a basic game loop (event handling, black screen clear/flip, delta-time clock capped at 60 FPS) plus periodic game state logging. A `CircleShape` base sprite class exists as a foundation for game objects, with a `draw` method that renders a shape's triangle outline. A `Player` class (triangle-shaped ship, positioned at screen center) extends `CircleShape` and can rotate in place with the `A`/`D` keys, updated each frame via `Player.update()`. Movement (thrust), asteroids, shooting, and collisions are not implemented yet.

## Controls

- `A` — rotate left
- `D` — rotate right

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
- `constants.py` — game constants (screen size, player radius, line width, turn speed, etc.)
- `logger.py` — writes periodic game state (`game_state.jsonl`) and event (`game_events.jsonl`) snapshots for debugging
- `circleshape.py` — `CircleShape`, a base `pygame.sprite.Sprite` class for circular game objects (position, velocity, radius)
- `player.py` — `Player`, extends `CircleShape` with a `triangle()` method describing the ship's shape, and `rotate()`/`update()` methods handling turn input each frame

## AI usage

AI (Claude Code) was used to help write this README, summarize implemented changes, and draft pull request summaries.
