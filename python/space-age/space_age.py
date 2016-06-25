class SpaceAge:
    EARTH_YEAR = 31557600
    PLANETS = {
        'Mercury': 0.2408467,
        'Venus': 0.61519726,
        'Mars': 1.8808158,
        'Jupiter': 11.862615,
        'Saturn': 29.447498,
        'Uranus': 84.016846,
        'Neptune': 164.79132,
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return self.seconds / SpaceAge.EARTH_YEAR
