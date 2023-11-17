class Settings():
    """a class to store all settings for alien invasion"""

    def __init__(self):
        """initialize the game's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0) 
        #ship settings
        self.ship_speed_factor = 1.5
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 5
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents
        self.fleet_direction = 1

