import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_ACCELERATION,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_RESPAWN_INVULNERABILITY_SECONDS,
    PLAYER_INVULNERABILITY_BLINK_HZ,
    LINE_WIDTH,
)
from shot import Shot

# Player Class - Inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.name = "Player"
        self.shot_cooldown = 0
        self.invulnerable_timer = 0.0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        # Blink while invulnerable instead of drawing every frame
        if self.is_invulnerable and int(self.invulnerable_timer * PLAYER_INVULNERABILITY_BLINK_HZ) % 2 == 0:
            return
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    @property
    def is_invulnerable(self) -> bool:
        return self.invulnerable_timer > 0

    def respawn(self, x: float, y: float) -> None:
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.invulnerable_timer = PLAYER_RESPAWN_INVULNERABILITY_SECONDS

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt: float)-> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.move(dt)
        self.shot_cooldown -= dt
        self.invulnerable_timer = max(0.0, self.invulnerable_timer - dt)

    def move(self, dt: float) -> None:
        # this method will take dt and apply thrust, accelerating/decelerating the
        # player's velocity, which is then applied to its position each frame
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        if keys[pygame.K_w]:
            # Thrust forward
            self.velocity += forward * PLAYER_ACCELERATION * dt
        if keys[pygame.K_s]:
            # Thrust backward
            self.velocity -= forward * PLAYER_ACCELERATION * dt
        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)
        self.position += self.velocity * dt

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    