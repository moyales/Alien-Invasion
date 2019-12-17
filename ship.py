import pygame

class Ship():

    def __init__(self, screen):
        '''Initialise the ship and its starting position'''
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load('C:/Users/matto/Documents/Programming/Python_Work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)