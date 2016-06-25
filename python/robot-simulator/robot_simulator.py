NORTH, EAST, SOUTH, WEST = (0, 1, 2, 3)
MOVEMENTS = {
            NORTH: (0, 1),
            EAST: (1, 0),
            SOUTH: (0, -1),
            WEST: (-1, 0),
            }


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = direction
        self.COMMANDS = {
                        'R': self.turn_right,
                        'L': self.turn_left,
                        'A': self.advance,
                        }

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        self.coordinates = tuple(sum(d) for d
                                 in zip(self.coordinates,
                                        MOVEMENTS[self.bearing]
                                        )
                                 )

    def simulate(self, command):
        for letter in command:
            self.COMMANDS[letter]()
