class Settings():
    '''A class to store the settings for Alien Invasion.'''

    def __init__(self):
        '''Initialise all the of the game's settings.'''
        # Screen Settings
        self.screen_width = 1200            # In pixels
        self.screen_height = 750
        self.bg_color = (51, 204, 255)      # RGB colors

        # Ship Settings
        self.ship_speed_factor = 0.8