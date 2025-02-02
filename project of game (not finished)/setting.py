import pygame
import sys
class Settings():
   
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (26, 0, 26)
        # Load an image
        image_path = "/Users/andymiaogu/Desktop/Andy's coding/projects/project of game (not finished)/outer-space-planets-background-d6dsvq0armnh3ajg.gif"  # Replace with the path to your image file
        self.image = pygame.image.load(image_path)
        
        
class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
    
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images.jpeg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False    
        self.moving_left = False       
    def update(self):
        #print(self.moving_right)
        if self.moving_right:
            self.rect.centerx +=10
        if self.moving_left:
            self.rect.centerx -=10
        
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

