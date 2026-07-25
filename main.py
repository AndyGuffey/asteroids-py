import sys

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_STARTING_LIVES
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import shot


set_mode = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, depth=0, display=0, vsync=0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0 
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable,)
player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()
shots = pygame.sprite.Group()
shot.Shot.containers = (updatable, drawable, shots)

def game_loop(screen, updatable, drawable, asteroids, shots):
    # `log_state()` inspects caller locals; keep `asteroids`/`shots` as local names so they get logged.
    dt = 0.0
    score = 0
    lives = PLAYER_STARTING_LIVES
    font = pygame.font.Font(None, 36)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for a in asteroids:
            if a.collides_with(player) and not player.is_invulnerable:
                lives -= 1
                log_event("player_hit", lives=lives, score=score)
                if lives <= 0:
                    print(f"Game over! Final score: {score}")
                    sys.exit()
                player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                log_event("player_respawn", lives=lives)
            for s in shots:
                if a.collides_with(s):
                    score += a.score_value()
                    log_event("asteroid_shot", score=score)
                    s.kill()
                    if a.split():
                        log_event("asteroid_split")
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        score_surface = font.render(f"Score: {score}", True, "white")
        lives_surface = font.render(f"Lives: {lives}", True, "white")
        screen.blit(score_surface, (10, 10))
        screen.blit(lives_surface, (10, 50))
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS
        # print(f"Delta time: {dt}") # debugging for delta time



def main():
    pygame.init()
    clock.tick(dt)
    game_loop(screen, updatable, drawable, asteroids, shots)



    print(f" Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    


if __name__ == "__main__":
    main()
