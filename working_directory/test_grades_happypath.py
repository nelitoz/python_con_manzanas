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


@pytest.mark.usefixtures('student', 'subject')
class TestHappyPath:
    pass
