import sys
import pygame
from pygame.sprite import Group

from python_space_game.settings import Settings
from python_space_game.ship import Ship
import python_space_game.game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        gf.update_screen(ai_settings, screen, ship, bullets)
        pygame.display.flip()


run_game()