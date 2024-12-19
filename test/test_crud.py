import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Student, Course, Enrollment

# Create a temporary in-memory SQLite database for testing
@pytest.fixture(scope="module")
def test_engine():
    engine = create_engine("sqlite:///:memory:")
    Student.metadata.create_all(engine)
    Course.metadata.create_all(engine)
    Enrollment.metadata.create_all(engine)
    yield engine
    Student.metadata.drop_all(engine)
    Course.metadata.drop_all(engine)
    Enrollment.metadata.drop_all(engine)

@pytest.fixture(scope="module")
def Session(test_engine):
    Session = sessionmaker(bind=test_engine)
    return Session

# ==================== Test CRUD for Students =========================

def test_add_student(Session):
    session = Session()
    new_student = Student(name="Alice Johnson", email="alice@example.com")
    session.add(new_student)
    session.commit()

    student = session.query(Student).filter_by(email="alice@example.com").first()
    assert student is not None
    assert student.name == "Alice Johnson"
    session.close()

def test_view_students(Session):
    session = Session()
    students = session.query(Student).all()
    assert len(students) > 0
    session.close()

def test_update_student(Session):
    session = Session()
    student = session.query(Student).filter_by(email="alice@example.com").first()
    student.name = "Alice J. Doe"
    session.commit()

    updated_student = session.query(Student).filter_by(name="Alice J. Doe").first()
    assert updated_student is not None
    session.close()

def test_delete_student(Session):
    session = Session()
    student = session.query(Student).filter_by(name="Alice J. Doe").first()
    session.delete(student)
    session.commit()

    deleted_student = session.query(Student).filter_by(name="Alice J. Doe").first()
    assert deleted_student is None
    session.close()

# ==================== Test CRUD for Courses =========================

def test_add_course(Session):
    session = Session()
    new_course = Course(title="Mathematics", description="An introduction to algebra.", instructor="Dr. Smith", capacity=30)
    session.add(new_course)
    session.commit()

    course = session.query(Course).filter_by(title="Mathematics").first()
    assert course is not None
    assert course.capacity == 30
    session.close()

def test_view_courses(Session):
    session = Session()
    courses = session.query(Course).all()
    assert len(courses) > 0
    session.close()

def test_update_course(Session):
    session = Session()
    course = session.query(Course).filter_by(title="Mathematics").first()
    course.instructor = "Prof. John Smith"
    session.commit()

    updated_course = session.query(Course).filter_by(instructor="Prof. John Smith").first()
    assert updated_course is not None
    session.close()

def test_delete_course(Session):
    session = Session()
    course = session.query(Course).filter_by(title="Mathematics").first()
    session.delete(course)
    session.commit()

    deleted_course = session.query(Course).filter_by(title="Mathematics").first()
    assert deleted_course is None
    session.close()

# ==================== Test Enrollment Management =========================

def test_enroll_student(Session):
    session = Session()
    student = Student(name="Bob Smith", email="bob@example.com")
    course = Course(title="Physics", description="Introduction to Physics.", instructor="Dr. Jane Doe", capacity=20)
    session.add_all([student, course])
    session.commit()

    enrollment = Enrollment(student_id=student.id, course_id=course.id, enrolled_at=datetime.utcnow())
    session.add(enrollment)
    session.commit()

    enrolled = session.query(Enrollment).filter_by(student_id=student.id, course_id=course.id).first()
    assert enrolled is not None
    assert enrolled.student_id == student.id
    assert enrolled.course_id == course.id
    session.close()

def test_view_enrollments(Session):
    session = Session()
    enrollments = session.query(Enrollment).all()
    assert len(enrollments) > 0
    session.close()

def test_remove_enrollment(Session):
    session = Session()
    enrollment = session.query(Enrollment).first()
    session.delete(enrollment)
    session.commit()

    deleted_enrollment = session.query(Enrollment).filter_by(id=enrollment.id).first()
    assert deleted_enrollment is None
    session.close()

# ==================== Running Tests ==============================

if __name__ == "__main__":
    pytest.main()
