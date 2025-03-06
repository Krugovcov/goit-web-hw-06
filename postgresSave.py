queries = {
    "query_1.sql": """
        SELECT students.name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        GROUP BY students.id
        ORDER BY average_grade DESC
        LIMIT 5;
    """,
    "query_2.sql": """
        SELECT students.name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'Математика'
        GROUP BY students.id
        ORDER BY average_grade DESC
        LIMIT 1;
    """,
    "query_3.sql": """
        SELECT groups.name AS group_name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN groups ON students.group_id = groups.id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'Математика'
        GROUP BY groups.name;
    """,
    "query_4.sql": """
        SELECT ROUND(AVG(grade), 2) AS average_grade
        FROM grades;
    """,
    "query_5.sql": """
        SELECT subjects.name
        FROM subjects
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE teachers.name = 'Іван Іванович'
        ORDER BY subjects.name;
    """,
    "query_6.sql": """
        SELECT students.name
        FROM students
        JOIN groups ON students.group_id = groups.id
        WHERE groups.name = 'Група A'
        ORDER BY students.name;
    """,
    "query_7.sql": """
        SELECT students.name, grades.grade, grades.date_received
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN groups ON students.group_id = groups.id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE groups.name = 'Група A'
        AND subjects.name = 'Математика'
        ORDER BY students.name;
    """,
    "query_8.sql": """
        SELECT teachers.name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE teachers.name = 'Іван Іванович'
        GROUP BY teachers.name;
    """,
    "query_9.sql": """
        SELECT subjects.name
        FROM subjects
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        WHERE students.name = 'Петро Петренко'
        ORDER BY subjects.name;
    """,
    "query_10.sql": """
        SELECT subjects.name
        FROM subjects
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE students.name = 'Петро Петренко'
        AND teachers.name = 'Іван Іванович'
        ORDER BY subjects.name;
    """
}

for filename, query in queries.items():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(query)
