import sys
import pygame
from setting import Settings
from setting import Ship
import game_functions as gf





def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption("Andy and Mr. Umair's Rocket game")
    bg_color = (360,360,360)
    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        # Watch for keyboard and mouse events.

        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship)
       
            
run_game()

