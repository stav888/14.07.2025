import os
import sqlite3

if os.path.exists('company.db'):
    os.remove('company.db')

conn = sqlite3.connect('company.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY(department_id) REFERENCES departments(department_id)
);
''')

cursor.executescript('''
INSERT INTO departments (department_id, name) VALUES
(1, 'Finance'), (2, 'IT'), (3, 'HR'), (4, 'Marketing');

INSERT INTO employees (employee_id, name, department_id) VALUES
(1, 'Shira', 1), (2, 'Doron', 2), (3, 'Tal', 2), (4, 'Adi', 3),
(5, 'Omer', NULL), (6, 'Yoni', 1), (7, 'Michal', NULL),
(8, 'Liad', 4), (9, 'Noga', 2), (10, 'Rami', 1);
''')

print("\n--- הצג את כל העובדים עם שם המחלקה שלהם ---")
cursor.execute('''
SELECT e.employee_id, e.name AS employee_name, d.name AS department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג את כל המחלקות וספור כמה עובדים יש לכל מחלקה ---")
cursor.execute('''
SELECT d.department_id, d.name AS department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.name
ORDER BY employee_count DESC
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג את כל העובדים כולל כאלה שלא שויכו למחלקה ---")
cursor.execute('''
SELECT e.employee_id, e.name AS employee_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IS NULL
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג מחלקות שאין בהן אף עובד ---")
cursor.execute('''
SELECT d.department_id, d.name AS department_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.employee_id IS NULL
''')
for row in cursor.fetchall():
    print(dict(row))

conn.commit()
conn.close()
