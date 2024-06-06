SELECT Student.student_name, Course.course_name
FROM Marks
INNER JOIN Student ON Marks.student_id = Student.student_id
INNER JOIN Course ON Marks.course_code = Course.course_code
WHERE Marks.marks >= 70;