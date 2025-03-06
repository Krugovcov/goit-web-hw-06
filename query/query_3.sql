
        SELECT groups.name AS group_name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN groups ON students.group_id = groups.id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.name = 'банк'
        GROUP BY groups.name;
    