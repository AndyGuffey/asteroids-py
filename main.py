import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT 

pygame.init()
set_mode = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=0, depth=0, display=0, vsync=0)

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    set_mode
    print(f" Screen width: {SCREEN_WIDTH} \n Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
