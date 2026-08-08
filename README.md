# Asteroids (Python)

A Python recreation of the classic Asteroids arcade game, built with [pygame](https://www.pygame.org/)

## Status

Playable core loop — fly a ship, shoot asteroids, and survive as long as possible. See [Project structure](#project-structure) below for how each piece is implemented.

- A basic intro menu (title, blinking "Press SPACE to start" prompt, and a controls reminder) is shown before the game begins
- Ship rotates and thrusts with momentum-based acceleration (capped at a max speed), fires rate-limited shots, is drawn in a distinct color (cyan) from asteroids/shots (white), and collides using its actual triangular shape rather than a bounding circle
- Asteroids spawn at random screen edges, split into smaller pieces when shot, and render as lumpy, non-circular polygons
- Asteroids and shots wrap around screen edges instead of disappearing (the player doesn't yet — see Future updates)
- Destroying an asteroid scores points (smaller asteroids are worth more), shown on screen, and triggers a brief particle explosion effect
- Player has multiple lives; getting hit respawns the ship at screen center with brief blinking invulnerability instead of ending the game immediately
- Player can drop a `Bomb` (rate-limited by its own cooldown), which sits in place and detonates after a short fuse, destroying every asteroid within its blast radius
- Game state and events are logged to `game_state.jsonl` / `game_events.jsonl` for debugging

## Controls

- `A` — rotate left
- `D` — rotate right
- `W` — thrust forward
- `S` — thrust backward
- `Space` — shoot (rate-limited by a cooldown; holding it down doesn't fire every frame)
- `B` — drop a bomb (rate-limited by its own cooldown)

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

- `main.py` — entry point; sets up the pygame window, sprite groups (`updatable`/`drawable`/`asteroid`), shows the intro menu, and runs the main game loop
- `menu.py` — `run_intro_menu()`, a blocking loop shown before gameplay starts that displays the title/prompt/controls and returns once the player presses `Space` (or `False` if the window is closed)
- `constants.py` — game constants (screen size, player radius, line width, turn speed, player speed/acceleration, lives/respawn invulnerability, asteroid sizes/spawn rate/shape, shot speed/cooldown, bomb fuse/blast radius/cooldown, scoring values, explosion effect, etc.)
- `logger.py` — writes periodic game state (`game_state.jsonl`) and event (`game_events.jsonl`) snapshots for debugging
- `circleshape.py` — `CircleShape`, a base `pygame.sprite.Sprite` class for circular game objects (position, velocity, radius), providing a shared `wrap_position()` for wrapping around screen edges and a `collides_with()` that tests against a triangular hitbox (via circle-triangle intersection) when the other object exposes a `triangle()` method, falling back to a plain circle-circle check otherwise
- `player.py` — `Player`, extends `CircleShape` with a `triangle()` method describing the ship's shape (and collision hitbox), `rotate()`/`move()`/`update()` methods handling turn and thrust input each frame, and `respawn()`/`is_invulnerable` for resetting the ship after a hit with temporary (blinking) invulnerability
- `asteroid.py` — `Asteroid`, extends `CircleShape` with its own `draw()`/`update()` overrides, rendering a lumpy polygon outline (via `_outline_points()`) that moves by its velocity and wraps around the screen edges, plus `score_value()` returning the points awarded for destroying it based on its size
- `asteroidfield.py` — `AsteroidField`, spawns `Asteroid`s at random screen edges with random size/speed/direction on a timer
- `shot.py` — `Shot`, extends `CircleShape` with its own `draw()`/`update()` for a bullet fired by the player that moves by its velocity and wraps around the screen edges
- `explosion.py` — `Explosion`, a short-lived particle burst spawned where an asteroid is destroyed; particles fly outward and shrink over `EXPLOSION_DURATION_SECONDS` before the sprite kills itself
- `bomb.py` — `Bomb`, extends `CircleShape`; dropped stationary at the player's position via `Player.drop_bomb()`, its `fuse_timer` counts down each update, and `is_detonating` tells the game loop when to destroy nearby asteroids and remove it

## Future updates

### Mechanics

- Make the player wrap around the screen instead of disappearing
- Create different weapon types
- Add a shield power-up
- Add a speed power-up

### Functionality

- Add a pause menu
  - Audio, Video settings options
- Add game over screen

### Art

- Add a background image
  - effects change based on power ups or lifes left

### Sound

- Add sound effects for shots, bombs, and explosions
- Add music while user is playing

## AI usage

AI (Claude Code) was used to help write this README, summarize implemented changes, and draft pull request summaries.
