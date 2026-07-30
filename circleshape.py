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
        # If `other` exposes a triangle() (e.g. the player ship), test against
        # its actual triangular hitbox instead of treating it as a circle.
        if hasattr(other, "triangle"):
            return self._intersects_triangle(other.triangle())
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)

    def _intersects_triangle(self, triangle: list[pygame.Vector2]) -> bool:
        a, b, c = triangle
        if self._point_in_triangle(self.position, a, b, c):
            return True
        for start, end in ((a, b), (b, c), (c, a)):
            closest = self._closest_point_on_segment(self.position, start, end)
            if self.position.distance_to(closest) < self.radius:
                return True
        return False

    @staticmethod
    def _closest_point_on_segment(
        point: pygame.Vector2, start: pygame.Vector2, end: pygame.Vector2
    ) -> pygame.Vector2:
        segment = end - start
        length_squared = segment.length_squared()
        if length_squared == 0:
            return start
        t = max(0.0, min(1.0, (point - start).dot(segment) / length_squared))
        return start + segment * t

    @staticmethod
    def _point_in_triangle(
        point: pygame.Vector2, a: pygame.Vector2, b: pygame.Vector2, c: pygame.Vector2
    ) -> bool:
        def sign(p1: pygame.Vector2, p2: pygame.Vector2, p3: pygame.Vector2) -> float:
            return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

        d1 = sign(point, a, b)
        d2 = sign(point, b, c)
        d3 = sign(point, c, a)
        has_neg = d1 < 0 or d2 < 0 or d3 < 0
        has_pos = d1 > 0 or d2 > 0 or d3 > 0
        return not (has_neg and has_pos)

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