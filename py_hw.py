import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('school.db')
cursor = connection.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
''')

# Insert data into students table
students_data = [
    (1, 'Emma'), (2, 'Liam'), (3, 'Olivia'), (4, 'Noah'), (5, 'Ava'),
    (6, 'William'), (7, 'Sophia'), (8, 'James'), (9, 'Mia'),
    (10, 'Benjamin'), (11, 'Zipi')
]

cursor.executemany('INSERT INTO students (student_id, name) VALUES (?, ?)', students_data)

# Insert data into courses table
courses_data = [
    (1, 'Mathematics'), (2, 'History'), (3, 'Physics'), (4, 'Literature'),
    (5, 'Biology'), (6, 'Chemistry'), (7, 'Art'), (8, 'Philosophy'),
    (9, 'Computer Science'), (10, 'Economics'), (11, 'Java beans')
]

cursor.executemany('INSERT INTO courses (course_id, title) VALUES (?, ?)', courses_data)

# Insert data into enrollments table
enrollments_data = [
    (1, 1), (1, 2), (1, 3), (2, 1), (2, 4), (2, 5), (3, 2), (3, 3),
    (3, 6), (4, 1), (4, 7), (4, 8), (5, 4), (5, 9), (6, 2), (6, 5),
    (6, 10), (7, 3), (7, 4), (8, 1), (8, 9), (9, 5), (9, 10),
    (10, 6), (10, 7), (10, 8)
]

cursor.executemany('INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)', enrollments_data)





# Query to show all enrollments with the student name and course name
cursor.execute('''
SELECT s.name AS student_name, c.title AS course_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;
''')

print("All enrollments with student name and course name:")
for row in cursor.fetchall():
    print(row)

# Query to show each student and count how many courses they have enrolled in
cursor.execute('''
SELECT s.name AS student_name, COUNT(e.course_id) AS course_count
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name;
''')

print("\nEach student and the count of courses they have enrolled in:")
for row in cursor.fetchall():
    print(row)

# Query to show each course and count how many students are enrolled
cursor.execute('''
SELECT c.title AS course_name, COUNT(e.student_id) AS student_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title;
''')

print("\nEach course and the count of students enrolled:")
for row in cursor.fetchall():
    print(row)

# Query to show courses with no students
cursor.execute('''
SELECT c.title AS course_name
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.student_id IS NULL;
''')

print("\nCourses with no students:")
for row in cursor.fetchall():
    print(row[0])

# Query to show students who did not enroll in any course
cursor.execute('''
SELECT s.name AS student_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;
''')

print("\nStudents who did not enroll in any course:")
for row in cursor.fetchall():
    print(row[0])

# Commit changes and close the connection
connection.commit()
connection.close()
