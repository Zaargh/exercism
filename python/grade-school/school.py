import collections


class School:

    def __init__(self, *args):
        self.grades_dict = collections.defaultdict(list)

    def grade(self, grade_no):
        return self.grades_dict[grade_no]

    def add(self, student, grade):
        self.grades_dict[grade].append(student)

    def sort(self):
        grades = sorted(k for k in self.grades_dict)
        for g in grades:
            yield g, tuple(sorted(self.grades_dict[g]))
