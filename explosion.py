import random

import pygame

from constants import (
    EXPLOSION_COLOR,
    EXPLOSION_PARTICLE_COUNT,
    EXPLOSION_PARTICLE_RADIUS,
    EXPLOSION_PARTICLE_SPEED_MIN,
    EXPLOSION_PARTICLE_SPEED_MAX,
    EXPLOSION_DURATION_SECONDS,
)


# A brief particle burst shown where an asteroid was destroyed
class Explosion(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float) -> None:
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.age = 0.0
        self.particle_offsets = [pygame.Vector2(0, 0) for _ in range(EXPLOSION_PARTICLE_COUNT)]
        self.particle_velocities = [
            pygame.Vector2(0, 1).rotate(random.uniform(0, 360))
            * random.uniform(EXPLOSION_PARTICLE_SPEED_MIN, EXPLOSION_PARTICLE_SPEED_MAX)
            for _ in range(EXPLOSION_PARTICLE_COUNT)
        ]

    def update(self, dt: float) -> None:
        self.age += dt
        if self.age >= EXPLOSION_DURATION_SECONDS:
            self.kill()
            return
        for i, velocity in enumerate(self.particle_velocities):
            self.particle_offsets[i] += velocity * dt

    def draw(self, screen: pygame.Surface) -> None:
        life_fraction = max(0.0, 1 - self.age / EXPLOSION_DURATION_SECONDS)
        radius = EXPLOSION_PARTICLE_RADIUS * life_fraction
        if radius <= 0:
            return
        for offset in self.particle_offsets:
            pygame.draw.circle(screen, EXPLOSION_COLOR, self.position + offset, radius)
