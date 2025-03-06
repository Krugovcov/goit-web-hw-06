
        SELECT subjects.name
        FROM subjects
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE students.name = 'Петро Петренко'
        AND teachers.name = 'Іван Іванович'
        ORDER BY subjects.name;
    