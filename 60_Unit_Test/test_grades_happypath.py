import pytest

@pytest.fixture
def student():
    from student import Student
    stud = Student('dacasti2 ragna')
    yield stud
    del stud
    
@pytest.fixture
def subject():
   from subject import Subject
   s = Subject("UnitTest 101")
   yield s
   del s

   
@pytest.mark.usefixtures('student', 'subject')
class TestHappyPath:
    def test_add_subject_to_student(self, student, subject):
        assert student.add_subject(subject) is True

    def test_add_grade_to_subject(self, student, subject):
        student.add_subject(subject)
        assert student.set_grade(subject, 10) is True

    def test_get_subject_grade(self,student,subject):
        student.add_subject(subject)
        student.set_grade(subject, 9)
        student.set_grade(subject, 8)
        assert student.get_grades_for_subject(subject) == [9,8]
