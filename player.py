import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_ACCELERATION,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)
from shot import Shot

# Player Class - Inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.name = "Player"
        self.shot_cooldown = 0

    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
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

    