# Shot class to handle the behavior of shots fired by the player in the game. It includes properties for position, velocity, and methods for updating the shot's position and checking for collisions with asteroids.
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.wrap_position()