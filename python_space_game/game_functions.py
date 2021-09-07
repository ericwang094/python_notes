import sys
import pygame


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            sys.exit()


def update_screen(ai_settings, screen, ship):

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()