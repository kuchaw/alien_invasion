class GameStats():
    """track statistics for Alien inavsion"""

    def __init__(self, ai_settings):
        """initialize statitistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #start alien invasion in an active state
        self.game_active = True

        #start game in an inactive state
        self.game_active = False 

    def reset_stats(self):
        """"initialize statisticss that can h¿change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0

