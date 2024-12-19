import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Course, Enrollment

engine = create_engine("sqlite:///enrollment_system.sqlite")
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# ==================== Student CRUD Operations ==========================

def add_student():
    name = input("Enter Student Name: ")
    email = input("Enter Student Email: ")

    student = Student(name=name, email=email, created_at=datetime.utcnow())
    session.add(student)
    session.commit()
    print("Student added successfully.")

def view_students():
    students = session.query(Student).all()
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"ID: {student.id} - Name: {student.name} - Email: {student.email}")

def update_student():
    student_id = int(input("Enter Student ID to update: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.name = input(f"Enter new name (current: {student.name}): ")
        student.email = input(f"Enter new email (current: {student.email}): ")
        session.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        session.delete(student)
        session.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")

# ==================== Course CRUD Operations ===========================

def add_course():
    title = input("Enter Course Title: ")
    description = input("Enter Course Description: ")
    instructor = input("Enter Instructor Name: ")
    capacity = int(input("Enter Course Capacity: "))

    course = Course(title=title, description=description, instructor=instructor, capacity=capacity, created_at=datetime.utcnow())
    session.add(course)
    session.commit()
    print("Course added successfully.")

def view_courses():
    courses = session.query(Course).all()
    if not courses:
        print("No courses found.")
    else:
        for course in courses:
            print(f"ID: {course.id} - Title: {course.title} - Instructor: {course.instructor} - Capacity: {course.capacity}")

def update_course():
    course_id = int(input("Enter Course ID to update: "))
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        course.title = input(f"Enter new title (current: {course.title}): ")
        course.description = input(f"Enter new description (current: {course.description}): ")
        course.instructor = input(f"Enter new instructor (current: {course.instructor}): ")
        course.capacity = int(input(f"Enter new capacity (current: {course.capacity}): "))
        session.commit()
        print("Course updated successfully.")
    else:
        print("Course not found.")

def delete_course():
    course_id = int(input("Enter Course ID to delete: "))
    course = session.query(Course).filter_by(id=course_id).first()
    if course:
        session.delete(course)
        session.commit()
        print("Course deleted successfully.")
    else:
        print("Course not found.")

# ==================== Enrollment Management ============================

def enroll_student():
    student_id = int(input("Enter Student ID to enroll: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found.")
        return

    course_id = int(input("Enter Course ID to enroll in: "))
    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        print("Course not found.")
        return

    if len(course.students) >= course.capacity:
        print("Course capacity reached. Cannot enroll more students.")
        return

    enrollment = Enrollment(student_id=student.id, course_id=course.id, enrolled_at=datetime.utcnow())
    session.add(enrollment)
    session.commit()
    print("Student enrolled successfully.")

def view_enrollments():
    student_id = int(input("Enter Student ID to view enrollments: "))
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        print("Student not found.")
    else:
        if not student.courses:
            print("This student is not enrolled in any courses.")
        else:
            for course in student.courses:
                print(f"Course ID: {course.id} - Title: {course.title} - Instructor: {course.instructor}")

def withdraw_student():
    student_id = int(input("Enter Student ID to withdraw: "))
    course_id = int(input("Enter Course ID to withdraw from: "))

    enrollment = session.query(Enrollment).filter_by(student_id=student_id, course_id=course_id).first()
    if enrollment:
        session.delete(enrollment)
        session.commit()
        print("Student withdrawn from course successfully.")
    else:
        print("Enrollment not found.")

# ===================== Main CLI App ===============================

def main():
    while True:
        os.system('clear')  # Clears the terminal screen (use 'cls' on Windows)
        print("Welcome to the Student Course Enrollment System")
        print("1. Manage Students")
        print("2. Manage Courses")
        print("3. Manage Enrollments")
        print("4. Exit")

        main_menu_choice = input("Enter your Choice: ")

        if main_menu_choice == '1':
            while True:
                os.system('clear')
                print("1. Add Student")
                print("2. View Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Back to Main Menu")

                student_menu_choice = input("Enter your Choice: ")

                if student_menu_choice == '1':
                    add_student()
                elif student_menu_choice == '2':
                    view_students()
                elif student_menu_choice == '3':
                    update_student()
                elif student_menu_choice == '4':
                    delete_student()
                elif student_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '2':
            while True:
                os.system('clear')
                print("1. Add Course")
                print("2. View Courses")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Back to Main Menu")

                course_menu_choice = input("Enter your Choice: ")

                if course_menu_choice == '1':
                    add_course()
                elif course_menu_choice == '2':
                    view_courses()
                elif course_menu_choice == '3':
                    update_course()
                elif course_menu_choice == '4':
                    delete_course()
                elif course_menu_choice == '5':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '3':
            while True:
                os.system('clear')
                print("1. Enroll Student")
                print("2. View Enrollments")
                print("3. Withdraw Student")
                print("4. Back to Main Menu")

                enrollment_menu_choice = input("Enter your Choice: ")

                if enrollment_menu_choice == '1':
                    enroll_student()
                elif enrollment_menu_choice == '2':
                    view_enrollments()
                elif enrollment_menu_choice == '3':
                    withdraw_student()
                elif enrollment_menu_choice == '4':
                    break
                input("Press Enter to continue...")

        elif main_menu_choice == '4':
            print("Goodbye!")
            session.close()
            break
        else:
            print("Invalid choice! Please choose again.")
            input("Press Enter to continue...")

# Call the main function
if __name__ == '__main__':
    main()
