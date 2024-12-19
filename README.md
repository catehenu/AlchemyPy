# AlchemyPy
# Student Course Enrollment System (CLI)

## Description

The **Student Course Enrollment System** is a CLI-based application designed to streamline the management of students, courses, and their enrollment records. It enables administrators to efficiently manage CRUD operations for students and courses while providing comprehensive features for enrolling students in courses and maintaining data consistency. The system leverages relationships between students and courses to simplify administration, reduce redundancy, and improve scalability.

---

## Problem Statement

Educational institutions face challenges in managing student enrollments as their scale grows. Using traditional methods such as spreadsheets or paper records often results in:

- Data redundancy and manual errors.
- Difficulty in tracking and updating enrollment data.
- Inefficiency in managing course capacities.
- Lack of scalability to accommodate growth.

---

## Proposed Solution

The **Student Course Enrollment System** offers a centralized solution to address these challenges. The system provides:

- **Student and Course Management:** Add, view, update, and delete student and course records.
- **Enrollment Management:** Enroll students in multiple courses and manage registrations.
- **Capacity Management:** Track course enrollment limits to avoid over-enrollment.
- **Data Integrity:** Enforce data consistency using well-defined relationships.
- **Scalability:** Handle larger datasets and support additional features like course prerequisites.

---

## Table Relationships

The system is structured with the following key relationships:

### 1. Students and Courses
- **Relationship:** Many-to-Many
- **Implementation:** Through an `Enrollments` junction table containing:
  - `id` (Primary Key)
  - `student_id` (Foreign Key to `Students`)
  - `course_id` (Foreign Key to `Courses`)

### 2. Courses and Students
- **Relationship:** Many-to-Many
- **Reverse Relationship:** Courses have multiple students, and students can enroll in multiple courses.

---

## User Stories

### Student Management
1. **Add a new student:** Allow administrators to create a student by providing their name and email.
2. **View all students:** Display a list of all students with their details.
3. **Update student details:** Edit student information such as name and email.
4. **Delete a student:** Remove a student from the system by their unique ID.

### Course Management
1. **Add a new course:** Create a course by specifying its title, description, and instructor details.
2. **View all courses:** Show a list of all courses with their titles and instructors.
3. **Update course details:** Modify the title, description, or instructor information.
4. **Delete a course:** Remove a course using its unique ID.

### Student Enrollment
1. **Enroll a student in a course:** Check course capacity before enrolling a student.
2. **View student enrollments:** List all courses a student is enrolled in.
3. **Withdraw a student from a course:** Remove a student’s enrollment from a specific course.

### Course Enrollment
1. **View students in a course:** List all students enrolled in a particular course.
2. **Check course capacity:** Ensure courses do not exceed maximum enrollment limits.
3. **Update enrollment status:** Add or remove students from courses as needed.

---

## System Design Considerations

### CRUD Operations
- Support Create, Read, Update, and Delete operations for all entities (students, courses, and enrollments).

### Enrollment Management
- Implement dynamic capacity checks to prevent over-enrollment.

### User Interface
- Provide a simple, user-friendly CLI for administrators.

### Scalability
- Design the system to accommodate features like course prerequisites and advanced search functionality.

### Data Integrity
- Enforce data consistency using foreign key constraints to ensure valid references between students, courses, and enrollments.

---

## Technical Stack

- **Programming Language:** Python
- **Database:** SQLite
- **CLI Framework:** Python’s `cmd` module or similar
- **Features:** Dynamic course capacity checks, exception handling for invalid inputs, and intuitive command navigation.

---

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
