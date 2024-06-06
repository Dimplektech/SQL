select student_name, last_name from Student 
INNER JOIN Course on Student.course_code=Course.course_code
where Course.course_code = 'DS03'
