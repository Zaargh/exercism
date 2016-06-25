from collections import namedtuple


class Garden:
    plant_dict = {
        'V': 'Violets',
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
    }

    def __init__(self, garden, students=None):
        if students is None:
            students = [
                'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred',
                'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
            ]
        self.garden = garden
        self.students = students

    def plants(self, student):
        pass
