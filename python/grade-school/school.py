import collections


class School:

    def __init__(self, *args):
        self.__grades_dict = collections.defaultdict(list)

    def grade(self, grade_no):
        return self.__grades_dict[grade_no]

    def add(self, student, grade):
        self.__grades_dict[grade].append(student)

    def sort(self):
        grades = sorted(k for k in self.__grades_dict)
        for g in grades:
            yield g, tuple(sorted(self.__grades_dict[g]))
