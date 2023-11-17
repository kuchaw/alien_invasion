class GameStats():
    """track statistics for Alien inavsion"""

    def __init__(self, ai_settings):
        """initialize statitistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """"initialize statisticss that can h¿change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        