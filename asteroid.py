import pygame
import random
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS,
    SCORE_ASTEROID_SMALL,
    SCORE_ASTEROID_MEDIUM,
    SCORE_ASTEROID_LARGE,
)

# Asteroid Class that inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

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