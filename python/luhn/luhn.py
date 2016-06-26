class Luhn:
    
    def __init__(self, number):
        self.number = number

    def addends(self):
        rev_digits = [int(i) for i in str(self.number)][::-1]
        not_multiplied = rev_digits[0::2]
        multiplied = [(i * 2)-(9 * ((i * 2) > 9)) for i in rev_digits[1::2]]
        return not_multiplied + multiplied

    def checksum(self):
        return sum(self.addends())

    def is_valid(self):
        return (self.checksum() % 10) == 0

    @staticmethod
    def create(n):
        rev_digits = [int(i) for i in str(n)][::-1]
        new_not_multiplied = rev_digits[1::2]
        new_multiplied = [(i * 2)-(9 * ((i * 2) > 9)) for i in rev_digits[0::2]]
        reminder = (10 - sum(new_multiplied + new_not_multiplied)) % 10
        return n * 10 + reminder
