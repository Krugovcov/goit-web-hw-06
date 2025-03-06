import psycopg2
from psycopg2 import sql
from faker import Faker
import random


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="newpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Створення Faker
faker = Faker("uk_UA")

# Видалення таблиць, якщо вони існують
cur.execute("""
    DROP TABLE IF EXISTS grades;
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS subjects;
    DROP TABLE IF EXISTS teachers;
    DROP TABLE IF EXISTS groups;
""")
conn.commit()

# Створення таблиць
cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );

    CREATE TABLE IF NOT EXISTS subjects (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        teacher_id INTEGER REFERENCES teachers(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        group_id INTEGER REFERENCES groups(id) ON DELETE SET NULL
    );

    CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
        subject_id INTEGER REFERENCES subjects(id) ON DELETE CASCADE,
        grade INTEGER CHECK (grade BETWEEN 1 AND 10),
        date_received DATE NOT NULL
    );
""")
conn.commit()

# Додавання груп з перевіркою на унікальність
groups = ["Група A", "Група B", "Група C"]
group_ids = []
for group in groups:
    # Перевірка чи група вже існує
    cur.execute("SELECT id FROM groups WHERE name = %s;", (group,))
    existing_group = cur.fetchone()

    if not existing_group:
        # Якщо групи немає, додаємо нову
        cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id;", (group,))
        group_ids.append(cur.fetchone()[0])

conn.commit()


teacher_ids = []
for _ in range(4):
    cur.execute("INSERT INTO teachers (name) VALUES (%s) RETURNING id;", (faker.name(),))
    teacher_ids.append(cur.fetchone()[0])

# Додавання предметів
subjects = [faker.word() for i in range(4)]
subject_ids = []
for subject in subjects:
    teacher_id = random.choice(teacher_ids)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id;", (subject, teacher_id))
    subject_ids.append(cur.fetchone()[0])

# Додавання студентів
student_ids = []
for _ in range(40):
    name = faker.name()
    group_id = random.choice(group_ids)
    cur.execute("INSERT INTO students (name, group_id) VALUES (%s, %s) RETURNING id;", (name, group_id))
    student_ids.append(cur.fetchone()[0])

# Додавання оцінок
for student_id in student_ids:
    for subject_id in subject_ids:
        for _ in range(random.randint(5, 15)):  # Випадкова кількість оцінок
            grade = random.randint(1, 10)
            date_received = faker.date_between(start_date="-1y", end_date="today")
            cur.execute("INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s);",
                        (student_id, subject_id, grade, date_received))

conn.commit()


cur.close()
conn.close()
