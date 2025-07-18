-- Create tables
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

-- Insert data
INSERT INTO departments (department_id, name) VALUES
(1, 'Finance'), (2, 'IT'), (3, 'HR'), (4, 'Marketing');

INSERT INTO employees (employee_id, name, department_id) VALUES
(1, 'Shira', 1), (2, 'Doron', 2), (3, 'Tal', 2), (4, 'Adi', 3),
(5, 'Omer', NULL), (6, 'Yoni', 1), (7, 'Michal', NULL),
(8, 'Liad', 4), (9, 'Noga', 2), (10, 'Rami', 1);

-- הצג את כל העובדים עם שם המחלקה שלהם
SELECT employees.employee_id, employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- הצג את כל המחלקות וספור כמה עובדים יש לכל מחלקה
SELECT departments.name, COUNT(employees.employee_id) AS number_of_employees
FROM departments
LEFT JOIN employees ON departments.department_id = employees.department_id
GROUP BY departments.name;

-- הצג את כל העובדים כולל כאלה שלא שויכו למחלקה
SELECT employees.employee_id, employees.name, departments.name AS department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.department_id;

-- הצג מחלקות שאין בהן אף עובד
SELECT departments.name
FROM departments
LEFT JOIN employees ON departments.department_id = employees.department_id
WHERE employees.employee_id IS NULL;
