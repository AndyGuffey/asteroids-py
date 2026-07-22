# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/)

## Status

Early stage — pygame is initialized and opens the game window, running a basic game loop (event handling, black screen clear/flip, delta-time clock capped at 60 FPS) plus periodic game state logging. A `CircleShape` base sprite class exists as a foundation for game objects, with a `draw` method that renders a shape's triangle outline. A `Player` class (triangle-shaped ship, positioned at screen center) extends `CircleShape` and can rotate with the `A`/`D` keys and thrust forward/backward with `W`/`S`, updated each frame via `Player.update()`. Sprites register into `updatable`/`drawable`/`asteroid` groups (via each class's `containers`) that the game loop updates and draws each frame. An `Asteroid` class (circle-shaped) extends `CircleShape` and moves by its velocity each update, and an `AsteroidField` spawns asteroids of random size, position, and velocity at the screen edges on a timer. Each frame, the game loop checks player/asteroid collisions; on a hit it logs a `player_hit` event, prints "Game over!", and exits. `Player` can fire a `Shot` with the spacebar, rate-limited by a shoot cooldown (`PLAYER_SHOOT_COOLDOWN_SECONDS`) so holding it down fires at a fixed rate rather than every frame. Each frame, the game loop also checks shot/asteroid collisions; on a hit it logs an `asteroid_shot` event, removes the shot, and calls `Asteroid.split()` on the asteroid — asteroids above the minimum radius split into two smaller, faster-moving asteroids (logging an `asteroid_split` event), while minimum-radius asteroids are simply destroyed. A basic scoring system awards points for each asteroid destroyed via `Asteroid.score_value()` — smaller, harder-to-hit asteroids are worth more (100/50/20 points for small/medium/large) — with the running score rendered in the top-left corner each frame and printed to the console on game over.

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
- `constants.py` — game constants (screen size, player radius, line width, turn speed, player speed, asteroid sizes/spawn rate, shot speed/cooldown, scoring values, etc.)
- `logger.py` — writes periodic game state (`game_state.jsonl`) and event (`game_events.jsonl`) snapshots for debugging
- `circleshape.py` — `CircleShape`, a base `pygame.sprite.Sprite` class for circular game objects (position, velocity, radius)
- `player.py` — `Player`, extends `CircleShape` with a `triangle()` method describing the ship's shape, and `rotate()`/`move()`/`update()` methods handling turn and thrust input each frame
- `asteroid.py` — `Asteroid`, extends `CircleShape` with its own `draw()`/`update()` overrides for a circular shape that moves by its velocity, plus `score_value()` returning the points awarded for destroying it based on its size
- `asteroidfield.py` — `AsteroidField`, spawns `Asteroid`s at random screen edges with random size/speed/direction on a timer
- `shot.py` — `Shot`, extends `CircleShape` with its own `draw()`/`update()` for a bullet fired by the player that moves by its velocity

## Future updates

- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

## AI usage

AI (Claude Code) was used to help write this README, summarize implemented changes, and draft pull request summaries.
