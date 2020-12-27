import subject


class Student:
    def __init__(self, name):
        self.name = name
        self.email = None
        self.subjects = []
        self.grades = []

    def add_subject(self, subject):
        pass

    def set_grade(self, subject, grade):
        pass

    def get_grades_for_subject(self, subject):
        pass
