
        SELECT students.name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'банк'
        GROUP BY students.id
        ORDER BY average_grade DESC
        LIMIT 1;
    