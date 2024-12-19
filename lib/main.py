from config import *
from models import Student, Course, Enrollment
from datetime import datetime

# Functions for CRUD Operations on Students
def add_student():
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")
    student = Student(name=name, email=email, created_at=datetime.utcnow())
    session = Session()
    session.add(student)
    session.commit()
    session.close()
    print("Student added successfully.")

def view_students():
    session = Session()
    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id} - Name: {student.name} - Email: {student.email}")
    session.close()

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = input(f"Enter new name (current: {student.name}): ")
        student.email = input(f"Enter new email (current: {student.email}): ")
        session.commit()
        session.close()
        print("Student updated successfully.")
    else:
        print("Student not found.")
        session.close()

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        session.close()
        print("Student deleted successfully.")
    else:
        print("Student not found.")
        session.close()

# Functions for CRUD Operations on Courses
def add_course():
    title = input("Enter Course Title: ")
    description = input("Enter Course Description: ")
    instructor = input("Enter Instructor Name: ")
    course = Course(title=title, description=description, instructor=instructor, created_at=datetime.utcnow())
    session = Session()
    session.add(course)
    session.commit()
    session.close()
    print("Course added successfully.")

def view_courses():
    session = Session()
    courses = session.query(Course).all()
    for course in courses:
        print(f"ID: {course.id} - Title: {course.title} - Instructor: {course.instructor}")
    session.close()

def update_course():
    course_id = int(input("Enter Course ID to update: "))
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.title = input(f"Enter new title (current: {course.title}): ")
        course.description = input(f"Enter new description (current: {course.description}): ")
        course.instructor = input(f"Enter new instructor (current: {course.instructor}): ")
        session.commit()
        session.close()
        print("Course updated successfully.")
    else:
        print("Course not found.")
        session.close()

def delete_course():
    course_id = int(input("Enter Course ID to delete: "))
    session = Session()
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        session.close()
        print("Course deleted successfully.")
    else:
        print("Course not found.")
        session.close()

# Functions for Enrollment Management
def enroll_student():
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    course = session.query(Course).filter_by(id=course_id).first()
    if student and course:
        enrollment = Enrollment(student_id=student_id, course_id=course_id, enrolled_at=datetime.utcnow())
        session.add(enrollment)
        session.commit()
        session.close()
        print("Student enrolled successfully.")
    else:
        print("Invalid Student or Course ID.")
        session.close()

def view_enrollments_by_student():
    student_id = int(input("Enter Student ID: "))
    session = Session()
    enrollments = session.query(Enrollment).filter_by(student_id=student_id).all()
    for enrollment in enrollments:
        course = session.query(Course).filter_by(id=enrollment.course_id).first()
        print(f"Course ID: {course.id} - Title: {course.title}")
    session.close()

def view_students_in_course():
    course_id = int(input("Enter Course ID: "))
    session = Session()
    enrollments = session.query(Enrollment).filter_by(course_id=course_id).all()
    for enrollment in enrollments:
        student = session.query(Student).filter_by(id=enrollment.student_id).first()
        print(f"Student ID: {student.id} - Name: {student.name}")
    session.close()

def withdraw_student():
    student_id = int(input("Enter Student ID: "))
    course_id = int(input("Enter Course ID: "))
    session = Session()
    enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment:
        session.delete(enrollment)
        session.commit()
        session.close()
        print("Student withdrawn successfully.")
    else:
        print("Enrollment record not found.")
        session.close()

# Main CLI App
def main():
    while True:
        print("Welcome to Student Course Enrollment System")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Manage Enrollments")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("1. Add Student")
                print("2. View Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back to Main Menu")
                student_choice = input("Enter your choice: ")
                if student_choice == '1':
                    add_student()
                elif student_choice == '2':
                    view_students()
                elif student_choice == '3':
                    update_student()
                elif student_choice == '4':
                    delete_student()
                elif student_choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == '2':
            while True:
                print("1. Add Course")
                print("2. View Courses")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Back to Main Menu")
                course_choice = input("Enter your choice: ")
                if course_choice == '1':
                    add_course()
                elif course_choice == '2':
                    view_courses()
                elif course_choice == '3':
                    update_course()
                elif course_choice == '4':
                    delete_course()
                elif course_choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == '3':
            while True:
                print("1. Enroll Student")
                print("2. View Enrollments by Student")
                print("3. View Students in Course")
                print("4. Withdraw Student")
                print("5. Back to Main Menu")
                enrollment_choice = input("Enter your choice: ")
                if enrollment_choice == '1':
                    enroll_student()
                elif enrollment_choice == '2':
                    view_enrollments_by_student()
                elif enrollment_choice == '3':
                    view_students_in_course()
                elif enrollment_choice == '4':
                    withdraw_student()
                elif enrollment_choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

# Run the application
if __name__ == "__main__":
    main()