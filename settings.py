class Settings():
    '''A class to store the settings for Alien Invasion.'''

    def __init__(self):
        '''Initialise all the of the game's settings.'''
        # Screen Settings
        self.screen_width = 1200            # In pixels
        self.screen_height = 750
        self.bg_color = (51, 204, 255)      # RGB colors

        # Ship Settings
        self.ship_speed_factor = 1.5

        # Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3