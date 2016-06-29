import random
from string import ascii_uppercase


class Robot:
    used_names = []

    def __init__(self):
        self.name = self.name_gen()

    def reset(self):
        self.name = self.name_gen()

    @staticmethod
    def name_gen():
        name = ''.join(random.choice(ascii_uppercase) for i in range(2)) + '{0:03}'.format(random.randint(0, 999))
        while name in Robot.used_names:
            name = ''.join(random.choice(ascii_uppercase) for i in range(2)) + '{0:03}'.format(random.randint(0, 999))
        Robot.used_names.append(name)
        return name
