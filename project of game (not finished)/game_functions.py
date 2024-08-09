import sys

import pygame
def check_events(ship):
     """Respond to keypresses and mouse events."""
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             sys.exit()
             
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 # Move the ship to the right.

                 ship.moving_right = True
                 
             if event.key == pygame.K_LEFT:
                 # Move the ship to the right.
                 ship.moving_left = True
   
                     
                 
         elif event.type == pygame.KEYUP:
             if event.key == pygame.K_RIGHT:
                 ship.moving_right = False   
             if event.key == pygame.K_LEFT:
                 ship.moving_left = False   
                 
         ship.update()
                 
                 
def update_screen(ai_settings, screen, ship):
     screen.blit(ai_settings.image,(0,0))
     ship.blitme()
     pygame.display.flip()