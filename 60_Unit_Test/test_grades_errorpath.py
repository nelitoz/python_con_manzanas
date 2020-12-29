import pytest

@pytest.fixture
def student():
    from student import Student
    stud = Student('Luka Zauber')
    yield stud
    del stud

@pytest.fixture
def subject():
    from subject import Subject
    s = Subject('Unit Testing 101')
    yield s
    del s

@pytest.fixture
def subjects():
    from subject import Subject
    s = [Subject('Unit Testing 101'), Subject('CS500')]
    yield s
    del s

@pytest.mark.usefixtures('student', 'subject')
class TestErrorPathSubject:
    def test_add_empty_subject_to_student(self, student, subject):
        assert student.add_subject(None) is False

    def test_add_existing_subject_to_student(self, student, subject):
        student.add_subject(subject)
        assert student.add_subject(subject) is False

@pytest.mark.usefixtures('student', 'subject')
class TestErrorPathAddGrade:
    def test_add_higher_grade_to_subject(self, student, subject):
        student.add_subject(subject)
        with pytest.raises(ValueError):
            student.set_grade(subject, 11)
    
    def test_add_lower_grade_to_subject(self, student, subject):
        student.add_subject(subject)
        with pytest.raises(ValueError):
            student.set_grade(subject, -1)

    def test_add_zero_grade_to_subject(self, student, subject):
        student.add_subject(subject)
        #with pytest.raises(ValueError):
        #    student.set_grade(subject, 0)
        assert student.set_grade(subject, 0) is False

@pytest.mark.usefixtures('student', 'subject', 'subjects')
class TestErrorPathGetGrade:
    def test_get_none_subject_grade(self, student, subject):
        student.add_subject(subject)
        student.set_grade(subject, 8)
        assert student.get_grades_for_subject(None) is False

    def test_get_missing_subject_grade(self, student, subjects):
        student.add_subject(subjects[0])
        student.add_subject(subjects[1])
        student.set_grade(subjects[0], 8)
        assert student.get_grades_for_subject(subjects[1]) == []

