import pygame
import random
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_VERTEX_COUNT,
    ASTEROID_RADIUS_VARIANCE,
    SCORE_ASTEROID_SMALL,
    SCORE_ASTEROID_MEDIUM,
    SCORE_ASTEROID_LARGE,
)

# Asteroid Class that inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        # Per-vertex radius multipliers, fixed at creation so the lumpy outline
        # doesn't jitter between frames. Collision still uses the plain circle radius.
        self.vertex_offsets = [
            random.uniform(1 - ASTEROID_RADIUS_VARIANCE, 1 + ASTEROID_RADIUS_VARIANCE)
            for _ in range(ASTEROID_VERTEX_COUNT)
        ]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self._outline_points(), LINE_WIDTH)

    def _outline_points(self) -> list[pygame.Vector2]:
        angle_step = 360 / ASTEROID_VERTEX_COUNT
        return [
            self.position
            + pygame.Vector2(0, 1).rotate(angle_step * i) * self.radius * offset
            for i, offset in enumerate(self.vertex_offsets)
        ]

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def score_value(self) -> int:
        # Smaller asteroids are worth more points since they're harder to hit
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_ASTEROID_SMALL
        if self.radius <= ASTEROID_MIN_RADIUS * 2:
            return SCORE_ASTEROID_MEDIUM
        return SCORE_ASTEROID_LARGE

    def split(self) -> list["Asteroid"]:
        # Imemediately kill itself
        self.kill()
        # If radius is < or equal to min radius just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        # Generate random angle between 20 & 50 degs
        angle1 = random.uniform(20, 50)
        # rotate velocity to create new velocity for first asteroid
        velocity1 = self.velocity.rotate(angle1)
        # rotate again for the second new asteroid, but in the opposite direction
        velocity2 = self.velocity.rotate(-angle1)
        # compute new radius of the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new asteroid objects at current position with new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        # Set firsts velovity to the first new vector, moving faster by scaling it 1.2
        asteroid1.velocity = velocity1 * 1.2
        # Same for the 2nd asteroid with new vector
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2

        return [asteroid1, asteroid2]