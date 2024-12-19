import unittest
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the base model
Base = declarative_base()

# Define the models for Students, Courses, and Enrollments
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    enrollments = relationship('Enrollment', back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    instructor = Column(String)
    capacity = Column(Integer, nullable=False)
    enrollments = relationship('Enrollment', back_populates='course')

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')

# Test Configuration
DATABASE_URL = "sqlite:///:memory:"

class TestEnrollmentSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(DATABASE_URL, echo=True)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        Base.metadata.drop_all(cls.engine)

    def test_add_student(self):
        student = Student(name="John Doe", email="john@example.com")
        self.session.add(student)
        self.session.commit()

        retrieved = self.session.query(Student).filter_by(email="john@example.com").first()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "John Doe")

    def test_add_course(self):
        course = Course(title="Math 101", description="Basic Math", instructor="Dr. Smith", capacity=30)
        self.session.add(course)
        self.session.commit()

        retrieved = self.session.query(Course).filter_by(title="Math 101").first()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.instructor, "Dr. Smith")

    def test_enroll_student_in_course(self):
        student = Student(name="Jane Doe", email="jane@example.com")
        course = Course(title="Science 101", description="Basic Science", instructor="Dr. Brown", capacity=25)
        self.session.add(student)
        self.session.add(course)
        self.session.commit()

        enrollment = Enrollment(student_id=student.id, course_id=course.id)
        self.session.add(enrollment)
        self.session.commit()

        retrieved = self.session.query(Enrollment).filter_by(student_id=student.id, course_id=course.id).first()
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.course.title, "Science 101")

    def test_course_capacity(self):
        course = Course(title="Physics 101", description="Basic Physics", instructor="Dr. Taylor", capacity=1)
        student1 = Student(name="Alice", email="alice@example.com")
        student2 = Student(name="Bob", email="bob@example.com")
        self.session.add(course)
        self.session.add_all([student1, student2])
        self.session.commit()

        enrollment1 = Enrollment(student_id=student1.id, course_id=course.id)
        self.session.add(enrollment1)
        self.session.commit()

        with self.assertRaises(Exception):
            enrollment2 = Enrollment(student_id=student2.id, course_id=course.id)
            self.session.add(enrollment2)
            self.session.commit()

    def test_remove_student_from_course(self):
        student = Student(name="Charlie", email="charlie@example.com")
        course = Course(title="History 101", description="Basic History", instructor="Dr. Green", capacity=20)
        self.session.add(student)
        self.session.add(course)
        self.session.commit()

        enrollment = Enrollment(student_id=student.id, course_id=course.id)
        self.session.add(enrollment)
        self.session.commit()

        self.session.delete(enrollment)
        self.session.commit()

        retrieved = self.session.query(Enrollment).filter_by(student_id=student.id, course_id=course.id).first()
        self.assertIsNone(retrieved)

if __name__ == "__main__":
    unittest.main()
