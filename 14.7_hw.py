CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    title TEXT
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO students (student_id, name) VALUES
(1, 'Emma'),
(2, 'Liam'),
(3, 'Olivia'),
(4, 'Noah'),
(5, 'Ava'),
(6, 'William'),
(7, 'Sophia'),
(8, 'James'),
(9, 'Mia'),
(10, 'Benjamin'),
(11, 'Zipi');

INSERT INTO courses (course_id, title) VALUES
(1, 'Mathematics'),
(2, 'History'),
(3, 'Physics'),
(4, 'Literature'),
(5, 'Biology'),
(6, 'Chemistry'),
(7, 'Art'),
(8, 'Philosophy'),
(9, 'Computer Science'),
(10, 'Economics'),
(11, 'Java beans');

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1), (1, 2), (1, 3),
(2, 1), (2, 4), (2, 5),
(3, 2), (3, 3), (3, 6),
(4, 1), (4, 7), (4, 8),
(5, 4), (5, 9),
(6, 2), (6, 5), (6, 10),
(7, 3), (7, 4),
(8, 1), (8, 9),
(9, 5), (9, 10),
(10, 6), (10, 7), (10, 8);

--	 show all enrollment with the student name + course name
SELECT s.name AS student_name, c.title AS course_name
FROM e
JOIN s ON e.student_id = s.student_id
JOIN c ON e.course_id = c.course_id;


-- 	show each student count how many course he has enrolled
SELECT s.name AS student_name, COUNT(e.course_id) AS course_count
FROM s
LEFT JOIN e ON s.student_id = e.student_id
GROUP BY s.student_id, s.name;


-- 	show each course count how many students enrolled
SELECT c.title AS course_name, COUNT(e.student_id) AS student_count
FROM c
LEFT JOIN e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title;


-- 	show courses with no studets
SELECT c.title AS course_name
FROM c
LEFT JOIN e ON c.course_id = e.course_id
WHERE e.student_id IS NULL;


-- 	show studetns which did not enroll
SELECT s.name AS student_name
FROM s
LEFT JOIN e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;
