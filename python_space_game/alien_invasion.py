import sys
import pygame

from python_space_game.settings import Settings
from python_space_game.ship import Ship
from python_space_game.game_functions import check_event, update_screen


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:
        check_event()

        update_screen(ai_settings, screen, ship)
        pygame.display.flip()

run_game()
