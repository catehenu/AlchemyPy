from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Many-to-Many relationship with courses via enrollments
    enrollments = relationship("Enrollment", back_populates="student")
    courses = relationship("Course", secondary="enrollments", back_populates="students")

# Define the Course model
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    instructor = Column(String(100), nullable=False)
    capacity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Many-to-Many relationship with students via enrollments
    enrollments = relationship("Enrollment", back_populates="course")
    students = relationship("Student", secondary="enrollments", back_populates="courses")

# Define the Enrollment model (junction table)
class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    enrolled_at = Column(DateTime, default=datetime.utcnow)

    # Relationships to Student and Course
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

# Relationships summary:
# Students and Courses have a Many-to-Many relationship via the Enrollment table.
