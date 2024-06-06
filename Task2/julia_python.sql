SELECT student_name,marks from Marks
INNER JOIN student on Student.student_id =Marks.student_id
INNER join Course on Marks.course_code = Course.course_code
where Course.teacher_name = 'Julia Python';