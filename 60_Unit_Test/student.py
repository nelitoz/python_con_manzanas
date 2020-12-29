import subject

class Student:
    def __init__(self, name):
        self.name = name
        self.email = None
        self.subjects = []
        self.grades = []

    def add_subject(self, subject):
        self.subject = subject
        if self.subject:
            if self.subject not in self.subjects:
                self.subjects.append(self.subject)
                return True
            else:
                return False
        else:
            return False

    def set_grade(self, subject, grade):
        if subject and grade!=0:
            if subject not in self.subjects:
                raise ValueError("No subject Found")
                
            if int(grade)<=10 and int(grade)>0:
                self.subject_grade = (subject,grade)
                if self.subject_grade not in self.grades:
                    self.grades.append(self.subject_grade)
                    return True
            else:
                raise ValueError("Wrong Grade")
        else:
            return False

    def get_grades_for_subject(self, subject):
        if subject:
            grades = []
            for grade in self.grades:
                if grade[0] is subject:
                    grades.append(grade[1])
        else:
            return False
        return grades
