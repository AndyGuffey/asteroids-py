# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/)

## Status

Playable core loop — fly a ship, shoot asteroids, and survive as long as possible. See [Project structure](#project-structure) below for how each piece is implemented.

- Ship rotates and thrusts with momentum-based acceleration (capped at a max speed), fires rate-limited shots, and is drawn in a distinct color (cyan) from asteroids/shots (white)
- Asteroids spawn at random screen edges, split into smaller pieces when shot, and render as lumpy, non-circular polygons
- Asteroids and shots wrap around screen edges instead of disappearing (the player doesn't yet — see Future updates)
- Destroying an asteroid scores points (smaller asteroids are worth more), shown on screen
- Player has multiple lives; getting hit respawns the ship at screen center with brief blinking invulnerability instead of ending the game immediately
- Game state and events are logged to `game_state.jsonl` / `game_events.jsonl` for debugging

## Controls

- `A` — rotate left
- `D` — rotate right
- `W` — thrust forward
- `S` — thrust backward
- `Space` — shoot (rate-limited by a cooldown; holding it down doesn't fire every frame)

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

- `main.py` — entry point; sets up the pygame window, sprite groups (`updatable`/`drawable`/`asteroid`), and runs the main game loop
- `constants.py` — game constants (screen size, player radius, line width, turn speed, player speed/acceleration, lives/respawn invulnerability, asteroid sizes/spawn rate/shape, shot speed/cooldown, scoring values, etc.)
- `logger.py` — writes periodic game state (`game_state.jsonl`) and event (`game_events.jsonl`) snapshots for debugging
- `circleshape.py` — `CircleShape`, a base `pygame.sprite.Sprite` class for circular game objects (position, velocity, radius), providing a shared `wrap_position()` for wrapping around screen edges
- `player.py` — `Player`, extends `CircleShape` with a `triangle()` method describing the ship's shape, `rotate()`/`move()`/`update()` methods handling turn and thrust input each frame, and `respawn()`/`is_invulnerable` for resetting the ship after a hit with temporary (blinking) invulnerability
- `asteroid.py` — `Asteroid`, extends `CircleShape` with its own `draw()`/`update()` overrides, rendering a lumpy polygon outline (via `_outline_points()`) that moves by its velocity and wraps around the screen edges, plus `score_value()` returning the points awarded for destroying it based on its size
- `asteroidfield.py` — `AsteroidField`, spawns `Asteroid`s at random screen edges with random size/speed/direction on a timer
- `shot.py` — `Shot`, extends `CircleShape` with its own `draw()`/`update()` for a bullet fired by the player that moves by its velocity and wraps around the screen edges

## Future updates

- Add an explosion effect for the asteroids
- Make the player wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

## AI usage

AI (Claude Code) was used to help write this README, summarize implemented changes, and draft pull request summaries.
