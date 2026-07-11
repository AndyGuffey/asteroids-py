import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player



set_mode = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, depth=0, display=0, vsync=0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0 
player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

def game_loop(screen, player):
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt =+ clock.tick(60) / 1000  # Limit the frame rate to 60 FPS
        # print(f"Delta time: {dt}") # debugging for delta time



def main():
    pygame.init()
    clock.tick(dt)
    game_loop(screen, player)
    
    
    
    print(f" Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    


if __name__ == "__main__":
    main()
