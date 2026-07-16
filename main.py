import sys

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

def game_loop(screen, updatable, drawable, asteroids):
    # `log_state()` inspects caller locals; keep `asteroids` as a local name so it gets logged.
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for a in asteroid:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS
        # print(f"Delta time: {dt}") # debugging for delta time



def main():
    pygame.init()
    clock.tick(dt)
    game_loop(screen, updatable, drawable, asteroids)



    print(f" Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    


if __name__ == "__main__":
    main()
