from faker import Faker
from datetime import datetime
from sqlalchemy.sql import func
from config import *  # Importing Session and engine configurations
from models import Student, Course, Enrollment  # Importing models

# Initialize Faker instance
fake = Faker()

# Create tables if they don't already exist
Student.metadata.create_all(engine)
Course.metadata.create_all(engine)
Enrollment.metadata.create_all(engine)

session = Session()

# Add some sample courses if none exist
course_titles = [
    "Introduction to Python",
    "Data Science Basics",
    "Web Development",
    "Database Management",
    "Artificial Intelligence",
]

for course_title in course_titles:
    # Check if the course already exists
    course = session.query(Course).filter_by(title=course_title).first()
    if not course:
        course = Course(
            title=course_title,
            description=fake.text(max_nb_chars=50),
            instructor=fake.name(),
            capacity=fake.random_int(min=10, max=30)
        )
        session.add(course)
        session.commit()

# Add some sample students if none exist
for _ in range(50):
    student = Student(
        name=fake.name(),
        email=fake.email(),
        created_at=datetime.utcnow()
    )
    session.add(student)

# Commit the students after they are added
session.commit()

# Add some sample enrollments
students = session.query(Student).all()
courses = session.query(Course).all()

for student in students:
    # Randomly enroll each student in 1-3 courses
    enrolled_courses = fake.random_elements(elements=courses, length=fake.random_int(min=1, max=3), unique=True)
    for course in enrolled_courses:
        # Check course capacity before enrolling
        current_enrollment = session.query(Enrollment).filter_by(course_id=course.id).count()
        if current_enrollment < course.capacity:
            enrollment = Enrollment(
                student_id=student.id,
                course_id=course.id,
                enrolled_at=datetime.utcnow()
            )
            session.add(enrollment)

# Commit the enrollments after they are added
session.commit()

print("Sample students, courses, and enrollments have been added successfully!")
