import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        '''Initialise the ship and its starting position'''
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('C:/Users/matto/Documents/Programming/Python_Work/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Update the ship's position based on the movement flags.'''
        # Update center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #if self.moving_up and self.rect.top < self.screen_rect.top:
        #    self.center += self.ai_settings.ship_speed_factor
        #if self.moving_down and self.rect.bottom > 0:
        #    self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center
        #self.rect.centery = self.center

    def blitme(self):
        '''draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Center the ship on the screen.'''
        self.center = self.screen_rect.centerx