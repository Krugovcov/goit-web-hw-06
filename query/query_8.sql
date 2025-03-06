
        SELECT teachers.name, ROUND(AVG(grades.grade), 2) AS average_grade
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN subjects ON grades.subject_id = subjects.id
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE teachers.name = 'Іван Іванович'
        GROUP BY teachers.name;
    