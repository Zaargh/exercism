import collections


class School:

    def __init__(self, school_name):
        self.grades = collections.defaultdict(list)

    def grade(self, grade_no):
        return self.grades[grade_no]

    def add(self, student, grade):
        self.grades[grade].append(student)
