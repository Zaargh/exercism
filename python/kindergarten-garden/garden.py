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
        self.students = sorted(students)
        self.garden_rows = self.garden.split('\n')

    def plants(self, student):
        student_pos = self.students.index(student)
        p = 2 * student_pos
        correct_plants = ''.join([row[p:p+2] for row in self.garden_rows])
        return [Garden.plant_dict[plant] for plant in correct_plants]