CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE passwords (
    user_id INTEGER UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

INSERT INTO users (user_id, name) VALUES
(1, 'Lior'), (2, 'Tamar'), (3, 'Erez'), (4, 'Dana'),
(5, 'Amit'), (6, 'Yael'), (7, 'Noam'), (8, 'Hila'),
(9, 'Aviad'), (10, 'Shani');

INSERT INTO passwords (user_id, password_hash) VALUES
(1, 'abc123'), (2, 'pass456'), (3, 'hello789'), (4, 'secure321'),
(5, 'qwerty12'), (6, 'secret99');

"""
  הצג את כל המשתמשים עם הסיסמה שלהם (INNER JOIN):
"""
SELECT users.user_id, users.name, passwords.password_hash
FROM users
INNER JOIN passwords ON users.user_id = passwords.user_id;

"""
הצג את כל המשתמשים, גם כאלה שאין להם סיסמה (LEFT JOIN):
"""
SELECT users.user_id, users.name, passwords.password_hash
FROM users
LEFT JOIN passwords ON users.user_id = passwords.user_id;

"""
הצג את המשתמשים שאין להם סיסמה כלל:
"""
SELECT users.user_id, users.name
FROM users
LEFT JOIN passwords ON users.user_id = passwords.user_id
WHERE passwords.user_id IS NULL;
