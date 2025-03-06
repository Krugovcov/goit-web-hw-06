
        SELECT students.name, grades.grade, grades.date_received
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN groups ON students.group_id = groups.id
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE groups.name = 'Група A'
        AND subjects.name = 'банк'
        ORDER BY students.name;
    