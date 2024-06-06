select email from Student
INNER JOIN Course on student.course_code=Course.course_code
where Course.course_level= '3';