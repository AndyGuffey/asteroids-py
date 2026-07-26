import pygame

from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(*self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
        pass

    def update(self, dt: float) -> None:
        # must override
        pass

    def collides_with(self,other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)

    def wrap_position(self) -> None:
        # Wrap around screen edges instead of drifting off into empty space,
        # using this shape's own radius so it's fully off-screen before it reappears
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius