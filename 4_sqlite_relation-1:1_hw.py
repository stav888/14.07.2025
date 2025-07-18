import os
import sqlite3

# Remove the existing database file if it exists
if os.path.exists('users.db'):
    os.remove('users.db')

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Use executescript to run multiple SQL statements at once
cursor.executescript('''
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE passwords (
    user_id INTEGER UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
''')

cursor.executescript('''
INSERT INTO users (user_id, name) VALUES
(1, 'Lior'), (2, 'Tamar'), (3, 'Erez'), (4, 'Dana'),
(5, 'Amit'), (6, 'Yael'), (7, 'Noam'), (8, 'Hila'),
(9, 'Aviad'), (10, 'Shani');

INSERT INTO passwords (user_id, password_hash) VALUES
(1, 'abc123'), (2, 'pass456'), (3, 'hello789'), (4, 'secure321'),
(5, 'qwerty12'), (6, 'secret99');
''')

# Display all users with their passwords using INNER JOIN
print("\n--- INNER JOIN: הצגת כל המשתמשים עם הסיסמאות שלהם ---")
cursor.execute('''
SELECT users.user_id, users.name, passwords.password_hash
FROM users
INNER JOIN passwords ON users.user_id = passwords.user_id;
''')

for row in cursor.fetchall():
    print(dict(row))

# Display all users, including those without passwords, using LEFT JOIN
print("\n--- LEFT JOIN: הצגת כל המשתמשים, גם אלה ללא סיסמה ---")
cursor.execute('''
SELECT users.user_id, users.name, passwords.password_hash
FROM users
LEFT JOIN passwords ON users.user_id = passwords.user_id;
''')

for row in cursor.fetchall():
    print(dict(row))

# Display users who do not have a password
print("\n--- הצגת המשתמשים שאין להם סיסמה כלל ---")
cursor.execute('''
SELECT users.user_id, users.name
FROM users
LEFT JOIN passwords ON users.user_id = passwords.user_id
WHERE passwords.user_id IS NULL;
''')

for row in cursor.fetchall():
    print(dict(row))

# Close the connection
conn.close()
