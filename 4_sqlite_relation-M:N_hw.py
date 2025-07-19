import os
import sqlite3

if os.path.exists('cable_tv.db'):
    os.remove('cable_tv.db')

conn = sqlite3.connect('cable_tv.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE citizens (
    citizen_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE cable_tv (
    company_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE subscriptions (
    citizen_id INTEGER,
    company_id INTEGER,
    PRIMARY KEY (citizen_id, company_id),
    FOREIGN KEY(citizen_id) REFERENCES citizens(citizen_id),
    FOREIGN KEY(company_id) REFERENCES cable_tv(company_id)
);

INSERT INTO citizens (citizen_id, name) VALUES
(1, 'Rina'), (2, 'Avi'), (3, 'Lea'), (4, 'Moshe'),
(5, 'Gali'), (6, 'Bar'), (7, 'Itai'), (8, 'Sivan'),
(9, 'Elior'), (10, 'Hodaya');

INSERT INTO cable_tv (company_id, name) VALUES
(1, 'HOT'), (2, 'YES'), (3, 'Partner TV');

INSERT INTO subscriptions (citizen_id, company_id) VALUES
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 1), (4, 1),
(5, 3), (6, 3), (6, 1),
(7, 2);
''')

print("\n--- הצג את כל המנויים עם שם האזרח ושם החברה ---")
cursor.execute('''
SELECT c.citizen_id, c.name AS citizen_name, ct.name AS company_name
FROM subscriptions s
JOIN citizens c ON s.citizen_id = c.citizen_id
JOIN cable_tv ct ON s.company_id = ct.company_id
ORDER BY c.citizen_id
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג את כל האזרחים וכמה חברות הם מנויים אליהן ---")
cursor.execute('''
SELECT c.citizen_id, c.name AS citizen_name, COUNT(s.company_id) AS subscription_count
FROM citizens c
LEFT JOIN subscriptions s ON c.citizen_id = s.citizen_id
GROUP BY c.citizen_id, c.name
ORDER BY c.citizen_id
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג את כל חברות הכבלים וכמה מנויים יש להן ---")
cursor.execute('''
SELECT ct.company_id, ct.name AS company_name, COUNT(s.citizen_id) AS subscriber_count
FROM cable_tv ct
LEFT JOIN subscriptions s ON ct.company_id = s.company_id
GROUP BY ct.company_id, ct.name
ORDER BY subscriber_count DESC
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג אזרחים שלא מנויים לאף חברה ---")
cursor.execute('''
SELECT c.citizen_id, c.name AS citizen_name
FROM citizens c
LEFT JOIN subscriptions s ON c.citizen_id = s.citizen_id
WHERE s.citizen_id IS NULL
''')
for row in cursor.fetchall():
    print(dict(row))

print("\n--- הצג חברות שאין להן אף מנוי ---")
cursor.execute('''
SELECT ct.company_id, ct.name AS company_name
FROM cable_tv ct
LEFT JOIN subscriptions s ON ct.company_id = s.company_id
WHERE s.company_id IS NULL
''')
for row in cursor.fetchall():
    print(dict(row))

conn.commit()
conn.close()
