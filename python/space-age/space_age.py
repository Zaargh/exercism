# TODO refactor to use setattr


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
        return round(float(self.seconds) / SpaceAge.EARTH_YEAR, 2)

    def __on_earth_wo_round(self):
        return float(self.seconds) / SpaceAge.EARTH_YEAR

    def __on_planet(self, planet):
        return round(self.__on_earth_wo_round() / SpaceAge.PLANETS[planet], 2)

    def on_mercury(self):
        return self.__on_planet('Mercury')

    def on_venus(self):
        return self.__on_planet('Venus')

    def on_mars(self):
        return self.__on_planet('Mars')

    def on_jupiter(self):
        return self.__on_planet('Jupiter')

    def on_saturn(self):
        return self.__on_planet('Saturn')

    def on_uranus(self):
        return self.__on_planet('Uranus')

    def on_neptune(self):
        return self.__on_planet('Neptune')
