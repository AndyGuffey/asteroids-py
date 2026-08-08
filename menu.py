import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def run_intro_menu(screen: pygame.Surface, clock: pygame.time.Clock) -> bool:
    # Shown before the game starts; returns True to begin play, False if the window was closed
    title_font = pygame.font.Font(None, 96)
    prompt_font = pygame.font.Font(None, 36)
    controls_font = pygame.font.Font(None, 28)

    title_surface = title_font.render("ASTEROIDS", True, "white")
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 80))

    prompt_surface = prompt_font.render("Press SPACE to start", True, "white")
    prompt_rect = prompt_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20))

    controls_lines = [
        "A / D - rotate        W / S - thrust",
        "SPACE - shoot        B - drop bomb",
    ]
    controls = []
    for i, line in enumerate(controls_lines):
        surface = controls_font.render(line, True, "gray")
        rect = surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90 + i * 28))
        controls.append((surface, rect))

    blink_timer = 0.0
    show_prompt = True
    while True:
        dt = clock.tick(60) / 1000
        blink_timer += dt
        if blink_timer >= 0.5:
            blink_timer = 0.0
            show_prompt = not show_prompt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True

        screen.fill("black")
        screen.blit(title_surface, title_rect)
        if show_prompt:
            screen.blit(prompt_surface, prompt_rect)
        for surface, rect in controls:
            screen.blit(surface, rect)
        pygame.display.flip()
